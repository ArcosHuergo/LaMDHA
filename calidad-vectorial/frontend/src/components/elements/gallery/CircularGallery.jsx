import { Camera, Mesh, Plane, Program, Renderer, Texture, Transform, Raycast, Vec2 } from 'ogl';
import { useEffect, useRef } from 'react';

import './CircularGallery.css';

function debounce(func, wait) {
  let timeout;
  return function (...args) {
    clearTimeout(timeout);
    timeout = setTimeout(() => func.apply(this, args), wait);
  };
}

function lerp(p1, p2, t) {
  return p1 + (p2 - p1) * t;
}

function autoBind(instance) {
  const proto = Object.getPrototypeOf(instance);
  Object.getOwnPropertyNames(proto).forEach(key => {
    if (key !== 'constructor' && typeof instance[key] === 'function') {
      instance[key] = instance[key].bind(instance);
    }
  });
}

// Figtree is not guaranteed to be available on the host page, so the component
// loads it on demand whenever the default font is used.
const DEFAULT_FONT_URL = 'https://fonts.googleapis.com/css2?family=Figtree:wght@400;700&display=swap';

function deriveFontFamilyFromUrl(url) {
  const fileName = (url.split('/').pop() || 'custom-font').split('?')[0];
  const base = fileName.replace(/\.(woff2?|ttf|otf|eot)$/i, '');
  return base.replace(/[^a-zA-Z0-9-_ ]/g, '').trim() || 'CircularGalleryFont';
}

async function loadFontFromStylesheet(url) {
  const response = await fetch(url);
  if (!response.ok) throw new Error(`Failed to fetch font stylesheet (${response.status})`);
  const cssText = await response.text();
  const faceBlocks = cssText.match(/@font-face\s*{[^}]*}/g) || [];
  let family = null;
  const fontFaces = [];
  for (const block of faceBlocks) {
    const familyMatch = block.match(/font-family:\s*['"]?([^;'"]+)['"]?/);
    const urlMatch = block.match(/url\(\s*['"]?([^'")]+)['"]?\s*\)/);
    if (!familyMatch || !urlMatch) continue;
    family = familyMatch[1].trim();
    const descriptors = {};
    const weightMatch = block.match(/font-weight:\s*([^;]+);/);
    const styleMatch = block.match(/font-style:\s*([^;]+);/);
    const rangeMatch = block.match(/unicode-range:\s*([^;]+);/);
    if (weightMatch) descriptors.weight = weightMatch[1].trim();
    if (styleMatch) descriptors.style = styleMatch[1].trim();
    if (rangeMatch) descriptors.unicodeRange = rangeMatch[1].trim();
    fontFaces.push(new FontFace(family, `url(${urlMatch[1]})`, descriptors));
  }
  if (!family) throw new Error('No @font-face rule found in the stylesheet');
  await Promise.allSettled(
    fontFaces.map(async face => {
      await face.load();
      document.fonts.add(face);
    })
  );
  return family;
}

async function loadFontFromFile(url) {
  const family = deriveFontFamilyFromUrl(url);
  const fontFace = new FontFace(family, `url(${url})`);
  await fontFace.load();
  document.fonts.add(fontFace);
  return family;
}

async function loadCustomFont(fontUrl) {
  const isStylesheet = fontUrl.includes('fonts.googleapis.com') || /\.css(\?.*)?$/i.test(fontUrl);
  return isStylesheet ? loadFontFromStylesheet(fontUrl) : loadFontFromFile(fontUrl);
}

// Loads `fontUrl` (a stylesheet such as a Google Fonts URL, or a direct font
// file) and returns a canvas-ready font string that keeps the size/weight from
// `font` but swaps in the freshly loaded family. Falls back to `font` on error.
async function resolveFont(font, fontUrl) {
  // Use the bundled Figtree stylesheet when the caller relies on the default
  // family (regardless of size/weight), otherwise honor the explicit `fontUrl`.
  const usesFigtreeDefault = /Figtree/i.test(font);
  const effectiveUrl = fontUrl || (usesFigtreeDefault ? DEFAULT_FONT_URL : null);
  if (!effectiveUrl) {
    // A custom family was supplied without a URL – make sure it is ready (in
    // case the host page declares it) before we draw it to the canvas,
    // otherwise the first paint silently falls back to a system font.
    if (document.fonts && document.fonts.load) {
      try {
        await document.fonts.load(font);
        await document.fonts.ready;
      } catch {
        // Ignore – fall back to whatever the browser provides.
      }
    }
    return font;
  }
  try {
    const family = await loadCustomFont(effectiveUrl);
    const sizeMatch = font.match(/^\s*(.*?\d+px)/);
    const prefix = sizeMatch ? sizeMatch[1].trim() : 'bold 30px';
    const resolved = `${prefix} "${family}"`;
    if (document.fonts && document.fonts.load) {
      try {
        await document.fonts.load(resolved);
      } catch {
        // Ignore – we still attempt to render with the requested font.
      }
    }
    return resolved;
  } catch (error) {
    console.error('CircularGallery: unable to load font from', fontUrl, error);
    return font;
  }
}

function getFontSize(font) {
  const match = font.match(/(\d+)px/);
  return match ? parseInt(match[1], 10) : 30;
}

// Draws a rounded-rect path on a 2D canvas context with an independent
// radius per corner (Safari/older browsers may not implement
// CanvasRenderingContext2D.roundRect natively, and it doesn't take
// per-corner radii as plain numbers in all engines anyway).
function traceRoundedRect(context, x, y, width, height, radii) {
  const uniform = typeof radii === 'number';
  const maxR = Math.min(width, height) / 2;
  const tl = Math.min(uniform ? radii : radii.tl || 0, maxR);
  const tr = Math.min(uniform ? radii : radii.tr || 0, maxR);
  const br = Math.min(uniform ? radii : radii.br || 0, maxR);
  const bl = Math.min(uniform ? radii : radii.bl || 0, maxR);

  context.beginPath();
  context.moveTo(x + tl, y);
  context.lineTo(x + width - tr, y);
  context.arcTo(x + width, y, x + width, y + tr, tr);
  context.lineTo(x + width, y + height - br);
  context.arcTo(x + width, y + height, x + width - br, y + height, br);
  context.lineTo(x + bl, y + height);
  context.arcTo(x, y + height, x, y + height - bl, bl);
  context.lineTo(x, y + tl);
  context.arcTo(x, y, x + tl, y, tl);
  context.closePath();
}

// Builds the caption bar that sits underneath each card: a solid/translucent
// rounded rectangle with the item's name centered on top of it.
function createCaptionTexture(
  gl,
  text,
  { font = 'bold 30px monospace', textColor = '#ffffff', backgroundColor = 'rgba(0, 0, 0, 0.65)', width = 600, height = 120, cornerRadius = 24 } = {}
) {
  const canvas = document.createElement('canvas');
  // Oversample a bit so the text stays crisp once the plane is scaled up.
  const dpr = 2;
  canvas.width = width * dpr;
  canvas.height = height * dpr;
  const context = canvas.getContext('2d');
  context.scale(dpr, dpr);
  context.clearRect(0, 0, width, height);

  traceRoundedRect(context, 0, 0, width, height, { tl: 0, tr: 0, br: cornerRadius, bl: cornerRadius });
  context.fillStyle = backgroundColor;
  context.fill();

  context.font = font;
  context.fillStyle = textColor;
  context.textBaseline = 'middle';
  context.textAlign = 'center';
  // Shrink the font until the label fits inside the bar with some padding.
  let resolvedFont = font;
  const maxTextWidth = width - 40;
  let metrics = context.measureText(text);
  let currentSize = getFontSize(font);
  while (metrics.width > maxTextWidth && currentSize > 12) {
    currentSize -= 1;
    resolvedFont = font.replace(/\d+px/, `${currentSize}px`);
    context.font = resolvedFont;
    metrics = context.measureText(text);
  }
  context.fillText(text, width / 2, height / 2);

  const texture = new Texture(gl, { generateMipmaps: false });
  texture.image = canvas;
  return { texture, width, height };
}

class Title {
  constructor({
    gl,
    plane,
    renderer,
    text,
    textColor = '#ffffff',
    backgroundColor = 'rgba(0, 0, 0, 0.65)',
    font = '30px sans-serif',
    heightRatio = 0.16,
    cornerRadius = 0.3,
    gap = 0
  }) {
    autoBind(this);
    this.gl = gl;
    this.plane = plane;
    this.renderer = renderer;
    this.text = text;
    this.textColor = textColor;
    this.backgroundColor = backgroundColor;
    this.font = font;
    this.heightRatio = heightRatio;
    this.cornerRadius = cornerRadius;
    this.gap = gap;
    this.createMesh();
  }
  createMesh() {
    // IMPORTANT: this mesh is parented to the card's plane, so its own
    // scale/position get multiplied by the plane's scale automatically when
    // the scene graph resolves world transforms. That means the values set
    // here must stay in *ratio* terms (relative to the plane's own 1x1 base
    // geometry), never the plane's current real-world scale — otherwise the
    // size gets applied twice (once here, once via the parent) and the bar
    // ends up either huge/off-screen or effectively invisible.
    const canvasHeight = 140;
    // Only used to size the source canvas so the text isn't stretched; safe
    // to read the plane's current scale here since it's just a ratio.
    const planeAspect = (this.plane.scale.x || 1) / ((this.plane.scale.y || 1) * this.heightRatio);
    const canvasWidth = Math.max(200, Math.round(canvasHeight * planeAspect));

    const { texture, width, height } = createCaptionTexture(this.gl, this.text, {
      font: this.font,
      textColor: this.textColor,
      backgroundColor: this.backgroundColor,
      width: canvasWidth,
      height: canvasHeight,
      cornerRadius: canvasHeight * this.cornerRadius
    });

    const geometry = new Plane(this.gl);
    const program = new Program(this.gl, {
      depthTest: false,
      depthWrite: false,
      vertex: `
        attribute vec3 position;
        attribute vec2 uv;
        uniform mat4 modelViewMatrix;
        uniform mat4 projectionMatrix;
        varying vec2 vUv;
        void main() {
          vUv = uv;
          gl_Position = projectionMatrix * modelViewMatrix * vec4(position, 1.0);
        }
      `,
      fragment: `
        precision highp float;
        uniform sampler2D tMap;
        varying vec2 vUv;
        void main() {
          vec4 color = texture2D(tMap, vUv);
          if (color.a < 0.02) discard;
          gl_FragColor = color;
        }
      `,
      uniforms: { tMap: { value: texture } },
      transparent: true
    });
    this.mesh = new Mesh(this.gl, { geometry, program });
    // Ratio-only: 1 = full width of the parent plane, heightRatio = fraction
    // of the plane's height. These stay constant no matter how big the plane
    // actually is on screen.
    this.mesh.scale.set(1, this.heightRatio, 1);
    this.mesh.position.y = -0.5 - this.heightRatio * 0.5 - this.gap;
    this.mesh.setParent(this.plane);
  }
  // Rebuilds the caption at the card's current size (called from onResize).
  update() {
    if (this.mesh) {
      this.mesh.setParent(null);
    }
    this.createMesh();
  }
}

class Media {
  constructor({
    geometry,
    gl,
    image,
    index,
    length,
    renderer,
    scene,
    screen,
    text,
    viewport,
    bend,
    captionTextColor,
    captionBackgroundColor,
    captionBorderRadius,
    highlightColor,
    borderRadius = 0,
    captionFont
  }) {
    this.extra = 0;
    this.geometry = geometry;
    this.gl = gl;
    this.image = image;
    this.index = index;
    this.length = length;
    this.renderer = renderer;
    this.scene = scene;
    this.screen = screen;
    this.text = text;
    this.viewport = viewport;
    this.bend = bend;
    this.captionTextColor = captionTextColor;
    this.captionBackgroundColor = captionBackgroundColor;
    this.captionBorderRadius = captionBorderRadius;
    this.highlightColor = highlightColor;
    this.borderRadius = borderRadius;
    this.captionFont = captionFont;
    this.selected = false;
    this.createShader();
    this.createMesh();
    this.createTitle();
    this.onResize();
  }
  createShader() {
    const texture = new Texture(this.gl, {
      generateMipmaps: true
    });
    this.program = new Program(this.gl, {
      depthTest: false,
      depthWrite: false,
      vertex: `
        precision highp float;
        attribute vec3 position;
        attribute vec2 uv;
        uniform mat4 modelViewMatrix;
        uniform mat4 projectionMatrix;
        uniform float uTime;
        uniform float uSpeed;
        varying vec2 vUv;
        void main() {
          vUv = uv;
          vec3 p = position;
          gl_Position = projectionMatrix * modelViewMatrix * vec4(p, 1.0);
        }
      `,
      fragment: `
        precision highp float;
        uniform vec2 uImageSizes;
        uniform vec2 uPlaneSizes;
        uniform sampler2D tMap;
        uniform float uBorderRadius;
        uniform float uSelected;
        uniform vec3 uHighlightColor;
        varying vec2 vUv;
        
        float sdRoundedBoxTopOnly(vec2 p, vec2 b, float r) {
          // Per-corner rounding (top-right, bottom-right, top-left, bottom-left).
          // Bottom corners get 0 radius so the image's lower edge is a
          // straight line that lines up exactly with the caption bar below.
          vec4 rad = vec4(r, 0.0, r, 0.0);
          rad.xy = (p.x > 0.0) ? rad.xy : rad.zw;
          float rr = (p.y > 0.0) ? rad.x : rad.y;
          vec2 q = abs(p) - b + rr;
          return min(max(q.x, q.y), 0.0) + length(max(q, 0.0)) - rr;
        }
        
        void main() {
          vec2 ratio = vec2(
            min((uPlaneSizes.x / uPlaneSizes.y) / (uImageSizes.x / uImageSizes.y), 1.0),
            min((uPlaneSizes.y / uPlaneSizes.x) / (uImageSizes.y / uImageSizes.x), 1.0)
          );
          vec2 uv = vec2(
            vUv.x * ratio.x + (1.0 - ratio.x) * 0.5,
            vUv.y * ratio.y + (1.0 - ratio.y) * 0.5
          );
          vec4 color = texture2D(tMap, uv);
          
          float d = sdRoundedBoxTopOnly(vUv - 0.5, vec2(0.5), uBorderRadius);
          
          // Smooth antialiasing for edges
          float edgeSmooth = 0.002;
          float alpha = 1.0 - smoothstep(-edgeSmooth, edgeSmooth, d);

          // Highlight ring drawn just inside the rounded edge when this card
          // is the selected/clicked one.
          if (uSelected > 0.5) {
            float borderWidth = 0.035;
            float borderMask = 1.0 - smoothstep(0.0, borderWidth, -d);
            borderMask *= step(d, 0.0);
            color.rgb = mix(color.rgb, uHighlightColor, borderMask * 0.9);
          }
          
          gl_FragColor = vec4(color.rgb, alpha);
        }
      `,
      uniforms: {
        tMap: { value: texture },
        uPlaneSizes: { value: [0, 0] },
        uImageSizes: { value: [0, 0] },
        uSpeed: { value: 0 },
        uTime: { value: 100 * Math.random() },
        uBorderRadius: { value: this.borderRadius },
        uSelected: { value: 0 },
        uHighlightColor: { value: this.highlightColor || [1.0, 0.85, 0.25] }
      },
      transparent: true
    });
    const img = new Image();
    img.crossOrigin = 'anonymous';
    img.src = this.image;
    img.onload = () => {
      texture.image = img;
      this.program.uniforms.uImageSizes.value = [img.naturalWidth, img.naturalHeight];
    };
  }
  createMesh() {
    this.plane = new Mesh(this.gl, {
      geometry: this.geometry,
      program: this.program
    });
    this.plane.setParent(this.scene);
  }
  createTitle() {
    this.title = new Title({
      gl: this.gl,
      plane: this.plane,
      renderer: this.renderer,
      text: this.text,
      textColor: this.captionTextColor,
      backgroundColor: this.captionBackgroundColor,
      cornerRadius: this.captionBorderRadius,
      font: this.captionFont
    });
  }
  setSelected(isSelected) {
    this.selected = isSelected;
    this.program.uniforms.uSelected.value = isSelected ? 1 : 0;
  }
  update(scroll, direction) {
    this.plane.position.x = this.x - scroll.current - this.extra;

    const x = this.plane.position.x;
    const H = this.viewport.width / 2;

    if (this.bend === 0) {
      this.plane.position.y = 0;
      this.plane.rotation.z = 0;
    } else {
      const B_abs = Math.abs(this.bend);
      const R = (H * H + B_abs * B_abs) / (2 * B_abs);
      const effectiveX = Math.min(Math.abs(x), H);

      const arc = R - Math.sqrt(R * R - effectiveX * effectiveX);
      if (this.bend > 0) {
        this.plane.position.y = -arc;
        this.plane.rotation.z = -Math.sign(x) * Math.asin(effectiveX / R);
      } else {
        this.plane.position.y = arc;
        this.plane.rotation.z = Math.sign(x) * Math.asin(effectiveX / R);
      }
    }

    this.speed = scroll.current - scroll.last;
    this.program.uniforms.uTime.value += 0.04;
    this.program.uniforms.uSpeed.value = this.speed;

    const planeOffset = this.plane.scale.x / 2;
    const viewportOffset = this.viewport.width / 2;
    this.isBefore = this.plane.position.x + planeOffset < -viewportOffset;
    this.isAfter = this.plane.position.x - planeOffset > viewportOffset;
    if (direction === 'right' && this.isBefore) {
      this.extra -= this.widthTotal;
      this.isBefore = this.isAfter = false;
    }
    if (direction === 'left' && this.isAfter) {
      this.extra += this.widthTotal;
      this.isBefore = this.isAfter = false;
    }
  }
  onResize({ screen, viewport } = {}) {
    if (screen) this.screen = screen;
    if (viewport) {
      this.viewport = viewport;
      if (this.plane.program.uniforms.uViewportSizes) {
        this.plane.program.uniforms.uViewportSizes.value = [this.viewport.width, this.viewport.height];
      }
    }
    this.scale = this.screen.height / 1500;
    this.plane.scale.y = (this.viewport.height * (900 * this.scale)) / this.screen.height;
    this.plane.scale.x = (this.viewport.width * (700 * this.scale)) / this.screen.width;
    this.plane.program.uniforms.uPlaneSizes.value = [this.plane.scale.x, this.plane.scale.y];
    if (this.title) this.title.update();
    this.padding = 2;
    this.width = this.plane.scale.x + this.padding;
    this.widthTotal = this.width * this.length;
    this.x = this.width * this.index;
  }
}

class App {
  constructor(
    container,
    {
      items,
      bend,
      captionTextColor = '#ffffff',
      captionBackgroundColor = 'rgba(0, 0, 0, 0.65)',
      captionBorderRadius = 0.3,
      highlightColor = [1.0, 0.85, 0.25],
      borderRadius = 0,
      captionFont = 'bold 22px Figtree',
      scrollSpeed = 2,
      scrollEase = 0.05,
      onItemClick
    } = {}
  ) {
    document.documentElement.classList.remove('no-js');
    this.container = container;
    this.scrollSpeed = scrollSpeed;
    this.scroll = { ease: scrollEase, current: 0, target: 0, last: 0 };
    this.onCheckDebounce = debounce(this.onCheck, 200);
    this.onItemClick = onItemClick;
    this.selectedMedia = null;
    this.raycast = new Raycast();
    this.mouse = new Vec2();
    this.createRenderer();
    this.createCamera();
    this.createScene();
    this.onResize();
    this.createGeometry();
    this.createMedias(
      items,
      bend,
      captionTextColor,
      captionBackgroundColor,
      captionBorderRadius,
      highlightColor,
      borderRadius,
      captionFont
    );
    this.update();
    this.addEventListeners();
  }
  createRenderer() {
    this.renderer = new Renderer({
      alpha: true,
      antialias: true,
      dpr: Math.min(window.devicePixelRatio || 1, 2)
    });
    this.gl = this.renderer.gl;
    this.gl.clearColor(0, 0, 0, 0);
    this.gl.canvas.style.cursor = 'grab';
    this.container.appendChild(this.gl.canvas);
  }
  createCamera() {
    this.camera = new Camera(this.gl);
    this.camera.fov = 45;
    this.camera.position.z = 20;
  }
  createScene() {
    this.scene = new Transform();
  }
  createGeometry() {
    this.planeGeometry = new Plane(this.gl, {
      heightSegments: 50,
      widthSegments: 100
    });
  }
  createMedias(
    items,
    bend = 1,
    captionTextColor,
    captionBackgroundColor,
    captionBorderRadius,
    highlightColor,
    borderRadius,
    captionFont
  ) {
    const defaultItems = [
      { image: `https://picsum.photos/seed/1/800/600?grayscale`, text: 'Bridge' },
      { image: `https://picsum.photos/seed/2/800/600?grayscale`, text: 'Desk Setup' },
      { image: `https://picsum.photos/seed/3/800/600?grayscale`, text: 'Waterfall' },
      { image: `https://picsum.photos/seed/4/800/600?grayscale`, text: 'Strawberries' },
      { image: `https://picsum.photos/seed/5/800/600?grayscale`, text: 'Deep Diving' },
      { image: `https://picsum.photos/seed/16/800/600?grayscale`, text: 'Train Track' },
      { image: `https://picsum.photos/seed/17/800/600?grayscale`, text: 'Santorini' },
      { image: `https://picsum.photos/seed/8/800/600?grayscale`, text: 'Blurry Lights' },
      { image: `https://picsum.photos/seed/9/800/600?grayscale`, text: 'New York' },
      { image: `https://picsum.photos/seed/10/800/600?grayscale`, text: 'Good Boy' },
      { image: `https://picsum.photos/seed/21/800/600?grayscale`, text: 'Coastline' },
      { image: `https://picsum.photos/seed/12/800/600?grayscale`, text: 'Palm Trees' }
    ];
    // Keep the original (non-duplicated) list around so click callbacks can
    // report a clean index/item back to the caller.
    this.galleryItems = items && items.length ? items : defaultItems;
    this.mediasImages = this.galleryItems.concat(this.galleryItems);
    this.medias = this.mediasImages.map((data, index) => {
      return new Media({
        geometry: this.planeGeometry,
        gl: this.gl,
        image: data.image,
        index,
        length: this.mediasImages.length,
        renderer: this.renderer,
        scene: this.scene,
        screen: this.screen,
        text: data.text,
        viewport: this.viewport,
        bend,
        captionTextColor,
        captionBackgroundColor,
        captionBorderRadius,
        highlightColor,
        borderRadius,
        captionFont
      });
    });
  }
  // Raycasts from a screen-space point into the scene and returns the Media
  // instance under it, if any.
  getMediaAtPoint(clientX, clientY) {
    if (!this.medias || !this.medias.length) return null;
    const rect = this.gl.canvas.getBoundingClientRect();
    this.mouse.set(
      ((clientX - rect.left) / rect.width) * 2 - 1,
      -((clientY - rect.top) / rect.height) * 2 + 1
    );
    this.raycast.castMouse(this.camera, this.mouse);
    const hits = this.raycast.intersectBounds(this.medias.map(media => media.plane));
    if (!hits.length) return null;
    return this.medias.find(media => media.plane === hits[0]) || null;
  }
  // Called on a real click (i.e. pointer didn't drag/scroll in between down
  // and up). Highlights the tapped card and fires the onItemClick callback,
  // similar to "selecting and submitting" that item.
  handleClick(clientX, clientY) {
    const media = this.getMediaAtPoint(clientX, clientY);
    if (!media) return;

    if (this.selectedMedia && this.selectedMedia !== media) {
      this.selectedMedia.setSelected(false);
    }
    media.setSelected(true);
    this.selectedMedia = media;

    if (typeof this.onItemClick === 'function') {
      const originalLength = this.galleryItems.length;
      const itemIndex = media.index % originalLength;
      this.onItemClick(this.galleryItems[itemIndex], itemIndex);
    }
  }
  onTouchDown(e) {
    this.isDown = true;
    this.hasDragged = false;
    this.scroll.position = this.scroll.current;
    this.start = e.touches ? e.touches[0].clientX : e.clientX;
    this.startY = e.touches ? e.touches[0].clientY : e.clientY;
    this.gl.canvas.style.cursor = 'grabbing';
  }
  onTouchMove(e) {
    const x = e.touches ? e.touches[0].clientX : e.clientX;
    const y = e.touches ? e.touches[0].clientY : e.clientY;

    if (!this.isDown) {
      // Hover feedback: show a pointer cursor when idling over a card.
      if (!e.touches) {
        const media = this.getMediaAtPoint(x, y);
        this.gl.canvas.style.cursor = media ? 'pointer' : 'grab';
      }
      return;
    }

    const distance = (this.start - x) * (this.scrollSpeed * 0.025);
    if (!this.hasDragged && (Math.abs(this.start - x) > 6 || Math.abs(this.startY - y) > 6)) {
      this.hasDragged = true;
    }
    this.scroll.target = this.scroll.position + distance;
  }
  onTouchUp(e) {
    this.isDown = false;
    this.gl.canvas.style.cursor = 'grab';
    this.onCheck();

    if (!this.hasDragged) {
      const point = e.changedTouches ? e.changedTouches[0] : e;
      this.handleClick(point.clientX, point.clientY);
    }
  }
  onWheel(e) {
    const delta = e.deltaY || e.wheelDelta || e.detail;
    this.scroll.target += (delta > 0 ? this.scrollSpeed : -this.scrollSpeed) * 0.2;
    this.onCheckDebounce();
  }
  onKeyDown(e) {
    switch (e.key) {
      case 'ArrowRight':
        e.preventDefault();
        this.scroll.target += this.scrollSpeed * 5;
        this.onCheckDebounce();
        break;

      case 'ArrowLeft':
        e.preventDefault();
        this.scroll.target -= this.scrollSpeed * 5;
        this.onCheckDebounce();
        break;

      case 'Home':
        e.preventDefault();
        this.scroll.target = 0;
        this.onCheckDebounce();
        break;

      default:
        break;
    }
  }

  onCheck() {
    if (!this.medias || !this.medias[0]) return;
    const width = this.medias[0].width;
    const itemIndex = Math.round(Math.abs(this.scroll.target) / width);
    const item = width * itemIndex;
    this.scroll.target = this.scroll.target < 0 ? -item : item;
  }
  onResize() {
    this.screen = {
      width: this.container.clientWidth,
      height: this.container.clientHeight
    };
    this.renderer.setSize(this.screen.width, this.screen.height);
    this.camera.perspective({
      aspect: this.screen.width / this.screen.height
    });
    const fov = (this.camera.fov * Math.PI) / 180;
    const height = 2 * Math.tan(fov / 2) * this.camera.position.z;
    const width = height * this.camera.aspect;
    this.viewport = { width, height };
    if (this.medias) {
      this.medias.forEach(media => media.onResize({ screen: this.screen, viewport: this.viewport }));
    }
  }
  update() {
    this.scroll.current = lerp(this.scroll.current, this.scroll.target, this.scroll.ease);
    const direction = this.scroll.current > this.scroll.last ? 'right' : 'left';
    if (this.medias) {
      this.medias.forEach(media => media.update(this.scroll, direction));
    }
    this.renderer.render({ scene: this.scene, camera: this.camera });
    this.scroll.last = this.scroll.current;
    this.raf = window.requestAnimationFrame(this.update.bind(this));
  }
  addEventListeners() {
    this.boundOnResize = this.onResize.bind(this);
    this.boundOnWheel = this.onWheel.bind(this);
    this.boundOnTouchDown = this.onTouchDown.bind(this);
    this.boundOnTouchMove = this.onTouchMove.bind(this);
    this.boundOnTouchUp = this.onTouchUp.bind(this);
    this.boundOnKeyDown = this.onKeyDown.bind(this);

    window.addEventListener('resize', this.boundOnResize);
    window.addEventListener('mousewheel', this.boundOnWheel);
    window.addEventListener('wheel', this.boundOnWheel);
    window.addEventListener('mousedown', this.boundOnTouchDown);
    window.addEventListener('mousemove', this.boundOnTouchMove);
    window.addEventListener('mouseup', this.boundOnTouchUp);
    window.addEventListener('touchstart', this.boundOnTouchDown);
    window.addEventListener('touchmove', this.boundOnTouchMove);
    window.addEventListener('touchend', this.boundOnTouchUp);

    this.container?.addEventListener('keydown', this.boundOnKeyDown);
  }
  destroy() {
    window.cancelAnimationFrame(this.raf);
    window.removeEventListener('resize', this.boundOnResize);
    window.removeEventListener('mousewheel', this.boundOnWheel);
    window.removeEventListener('wheel', this.boundOnWheel);
    window.removeEventListener('mousedown', this.boundOnTouchDown);
    window.removeEventListener('mousemove', this.boundOnTouchMove);
    window.removeEventListener('mouseup', this.boundOnTouchUp);
    window.removeEventListener('touchstart', this.boundOnTouchDown);
    window.removeEventListener('touchmove', this.boundOnTouchMove);
    window.removeEventListener('touchend', this.boundOnTouchUp);
    if (this.renderer && this.renderer.gl && this.renderer.gl.canvas.parentNode) {
      this.renderer.gl.canvas.parentNode.removeChild(this.renderer.gl.canvas);
    }

    if (this.container) {
      this.container.removeEventListener('keydown', this.boundOnKeyDown);
    }
  }
}

export default function CircularGallery({
  items,
  bend = 3,
  // Caption bar (the rectangle glued to the bottom of each card)
  captionTextColor = '#ffffff',
  captionBackgroundColor = 'rgba(0, 0, 0, 0.65)',
  captionBorderRadius = 0.3, // 0 (square) – 0.5 (pill), relative to the bar's own height
  captionFontFamily = 'Figtree',
  captionFontSize = 22, // px
  captionFontWeight = 'bold',
  highlightColor = '#ffd940',
  borderRadius = 0.05,
  fontUrl,
  scrollSpeed = 2,
  scrollEase = 0.05,
  onItemClick
}) {
  const containerRef = useRef(null);
  useEffect(() => {
    if (!containerRef.current) return;
    let app;
    let isMounted = true;
    const captionFont = `${captionFontWeight} ${captionFontSize}px ${captionFontFamily}`;

    // Convert '#rrggbb' (or 'rgb()'/'rgba()') highlight colors into the
    // 0-1 float triplet the fragment shader expects.
    const resolveHighlightRgb = color => {
      if (Array.isArray(color)) return color;
      const ctx = document.createElement('canvas').getContext('2d');
      ctx.fillStyle = color;
      const computed = ctx.fillStyle;
      const match = computed.match(/^#([0-9a-f]{6})$/i);
      if (match) {
        const int = parseInt(match[1], 16);
        return [((int >> 16) & 255) / 255, ((int >> 8) & 255) / 255, (int & 255) / 255];
      }
      return [1.0, 0.85, 0.25];
    };

    resolveFont(captionFont, fontUrl).then(resolvedFont => {
      if (!isMounted || !containerRef.current) return;
      app = new App(containerRef.current, {
        items,
        bend,
        captionTextColor,
        captionBackgroundColor,
        captionBorderRadius,
        highlightColor: resolveHighlightRgb(highlightColor),
        borderRadius,
        captionFont: resolvedFont,
        scrollSpeed,
        scrollEase,
        onItemClick
      });
    });

    return () => {
      isMounted = false;
      if (app) app.destroy();
    };
  }, [
    items,
    bend,
    captionTextColor,
    captionBackgroundColor,
    captionBorderRadius,
    captionFontFamily,
    captionFontSize,
    captionFontWeight,
    highlightColor,
    borderRadius,
    fontUrl,
    scrollSpeed,
    scrollEase,
    onItemClick
  ]);
  return (
    <div
      className="circular-gallery"
      ref={containerRef}
      tabIndex={0}
      role="region"
      aria-label="Circular image gallery. Use left and right arrow keys to navigate. Press on a card to select it."
    />
  );
}