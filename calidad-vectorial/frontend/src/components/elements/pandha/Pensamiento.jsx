import './Pensamiento.css';

/**
 * Burbuja de pensamiento pixel art (misma paleta, borde blanco y tamaño de pixel que el sprite del Pandha).
 * Aparece en secuencia: burbuja chica → mediana → nube, y los puntos "piensan" adentro.
 * El tamaño se controla con la variable CSS --px (tamaño de un pixel del dibujo).
 */
export const Pensamiento = ({ className = '' }) => {
    return (
        <svg
            className={`pensamiento ${className}`}
            viewBox="0 0 34 28"
            shapeRendering="crispEdges"
            aria-hidden="true"
        >
            <g className="pensamiento__chica">
                <rect x="2" y="23" width="3" height="1" fill="#ffffff" />
                <rect x="1" y="24" width="1" height="1" fill="#ffffff" />
                <rect x="5" y="24" width="1" height="1" fill="#ffffff" />
                <rect x="1" y="25" width="1" height="1" fill="#ffffff" />
                <rect x="5" y="25" width="1" height="1" fill="#ffffff" />
                <rect x="1" y="26" width="1" height="1" fill="#ffffff" />
                <rect x="5" y="26" width="1" height="1" fill="#ffffff" />
                <rect x="2" y="27" width="3" height="1" fill="#ffffff" />
                <rect x="2" y="24" width="3" height="1" fill="#070707" />
                <rect x="2" y="25" width="1" height="1" fill="#070707" />
                <rect x="4" y="25" width="1" height="1" fill="#070707" />
                <rect x="2" y="26" width="3" height="1" fill="#070707" />
                <rect x="3" y="25" width="1" height="1" fill="#fdf6e7" />
            </g>
            <g className="pensamiento__media">
                <rect x="6" y="18" width="4" height="1" fill="#ffffff" />
                <rect x="5" y="19" width="1" height="1" fill="#ffffff" />
                <rect x="10" y="19" width="1" height="1" fill="#ffffff" />
                <rect x="5" y="20" width="1" height="1" fill="#ffffff" />
                <rect x="10" y="20" width="1" height="1" fill="#ffffff" />
                <rect x="4" y="21" width="1" height="1" fill="#ffffff" />
                <rect x="11" y="21" width="1" height="1" fill="#ffffff" />
                <rect x="5" y="22" width="1" height="1" fill="#ffffff" />
                <rect x="10" y="22" width="1" height="1" fill="#ffffff" />
                <rect x="5" y="23" width="1" height="1" fill="#ffffff" />
                <rect x="10" y="23" width="1" height="1" fill="#ffffff" />
                <rect x="6" y="24" width="4" height="1" fill="#ffffff" />
                <rect x="6" y="19" width="4" height="1" fill="#070707" />
                <rect x="6" y="20" width="1" height="1" fill="#070707" />
                <rect x="9" y="20" width="1" height="1" fill="#070707" />
                <rect x="5" y="21" width="1" height="1" fill="#070707" />
                <rect x="10" y="21" width="1" height="1" fill="#070707" />
                <rect x="6" y="22" width="1" height="1" fill="#070707" />
                <rect x="9" y="22" width="1" height="1" fill="#070707" />
                <rect x="6" y="23" width="4" height="1" fill="#070707" />
                <rect x="7" y="20" width="2" height="1" fill="#fdf6e7" />
                <rect x="6" y="21" width="4" height="1" fill="#fdf6e7" />
                <rect x="7" y="22" width="2" height="1" fill="#fdf6e7" />
            </g>
            <g className="pensamiento__nube">
                <rect x="16" y="0" width="4" height="1" fill="#ffffff" />
                <rect x="14" y="1" width="2" height="1" fill="#ffffff" />
                <rect x="20" y="1" width="2" height="1" fill="#ffffff" />
                <rect x="13" y="2" width="1" height="1" fill="#ffffff" />
                <rect x="22" y="2" width="1" height="1" fill="#ffffff" />
                <rect x="9" y="3" width="4" height="1" fill="#ffffff" />
                <rect x="23" y="3" width="4" height="1" fill="#ffffff" />
                <rect x="8" y="4" width="1" height="1" fill="#ffffff" />
                <rect x="27" y="4" width="1" height="1" fill="#ffffff" />
                <rect x="7" y="5" width="1" height="1" fill="#ffffff" />
                <rect x="28" y="5" width="1" height="1" fill="#ffffff" />
                <rect x="6" y="6" width="1" height="1" fill="#ffffff" />
                <rect x="29" y="6" width="1" height="1" fill="#ffffff" />
                <rect x="6" y="7" width="1" height="1" fill="#ffffff" />
                <rect x="29" y="7" width="1" height="1" fill="#ffffff" />
                <rect x="6" y="8" width="1" height="1" fill="#ffffff" />
                <rect x="29" y="8" width="1" height="1" fill="#ffffff" />
                <rect x="6" y="9" width="1" height="1" fill="#ffffff" />
                <rect x="29" y="9" width="1" height="1" fill="#ffffff" />
                <rect x="6" y="10" width="1" height="1" fill="#ffffff" />
                <rect x="29" y="10" width="1" height="1" fill="#ffffff" />
                <rect x="6" y="11" width="1" height="1" fill="#ffffff" />
                <rect x="29" y="11" width="1" height="1" fill="#ffffff" />
                <rect x="7" y="12" width="1" height="1" fill="#ffffff" />
                <rect x="28" y="12" width="1" height="1" fill="#ffffff" />
                <rect x="8" y="13" width="1" height="1" fill="#ffffff" />
                <rect x="27" y="13" width="1" height="1" fill="#ffffff" />
                <rect x="9" y="14" width="1" height="1" fill="#ffffff" />
                <rect x="26" y="14" width="1" height="1" fill="#ffffff" />
                <rect x="10" y="15" width="1" height="1" fill="#ffffff" />
                <rect x="25" y="15" width="1" height="1" fill="#ffffff" />
                <rect x="10" y="16" width="1" height="1" fill="#ffffff" />
                <rect x="25" y="16" width="1" height="1" fill="#ffffff" />
                <rect x="11" y="17" width="2" height="1" fill="#ffffff" />
                <rect x="17" y="17" width="2" height="1" fill="#ffffff" />
                <rect x="23" y="17" width="2" height="1" fill="#ffffff" />
                <rect x="13" y="18" width="4" height="1" fill="#ffffff" />
                <rect x="19" y="18" width="4" height="1" fill="#ffffff" />
                <rect x="16" y="1" width="4" height="1" fill="#070707" />
                <rect x="14" y="2" width="2" height="1" fill="#070707" />
                <rect x="20" y="2" width="2" height="1" fill="#070707" />
                <rect x="13" y="3" width="1" height="1" fill="#070707" />
                <rect x="22" y="3" width="1" height="1" fill="#070707" />
                <rect x="9" y="4" width="4" height="1" fill="#070707" />
                <rect x="23" y="4" width="4" height="1" fill="#070707" />
                <rect x="8" y="5" width="1" height="1" fill="#070707" />
                <rect x="27" y="5" width="1" height="1" fill="#070707" />
                <rect x="7" y="6" width="1" height="1" fill="#070707" />
                <rect x="28" y="6" width="1" height="1" fill="#070707" />
                <rect x="7" y="7" width="1" height="1" fill="#070707" />
                <rect x="28" y="7" width="1" height="1" fill="#070707" />
                <rect x="7" y="8" width="1" height="1" fill="#070707" />
                <rect x="28" y="8" width="1" height="1" fill="#070707" />
                <rect x="7" y="9" width="1" height="1" fill="#070707" />
                <rect x="28" y="9" width="1" height="1" fill="#070707" />
                <rect x="7" y="10" width="1" height="1" fill="#070707" />
                <rect x="28" y="10" width="1" height="1" fill="#070707" />
                <rect x="7" y="11" width="1" height="1" fill="#070707" />
                <rect x="28" y="11" width="1" height="1" fill="#070707" />
                <rect x="8" y="12" width="1" height="1" fill="#070707" />
                <rect x="27" y="12" width="1" height="1" fill="#070707" />
                <rect x="9" y="13" width="1" height="1" fill="#070707" />
                <rect x="26" y="13" width="1" height="1" fill="#070707" />
                <rect x="10" y="14" width="1" height="1" fill="#070707" />
                <rect x="25" y="14" width="1" height="1" fill="#070707" />
                <rect x="11" y="15" width="1" height="1" fill="#070707" />
                <rect x="24" y="15" width="1" height="1" fill="#070707" />
                <rect x="11" y="16" width="2" height="1" fill="#070707" />
                <rect x="17" y="16" width="2" height="1" fill="#070707" />
                <rect x="23" y="16" width="2" height="1" fill="#070707" />
                <rect x="13" y="17" width="4" height="1" fill="#070707" />
                <rect x="19" y="17" width="4" height="1" fill="#070707" />
                <rect x="8" y="10" width="1" height="1" fill="#c2bcb6" />
                <rect x="27" y="10" width="1" height="1" fill="#c2bcb6" />
                <rect x="8" y="11" width="2" height="1" fill="#c2bcb6" />
                <rect x="26" y="11" width="2" height="1" fill="#c2bcb6" />
                <rect x="9" y="12" width="2" height="1" fill="#c2bcb6" />
                <rect x="25" y="12" width="2" height="1" fill="#c2bcb6" />
                <rect x="10" y="13" width="2" height="1" fill="#c2bcb6" />
                <rect x="24" y="13" width="2" height="1" fill="#c2bcb6" />
                <rect x="11" y="14" width="2" height="1" fill="#c2bcb6" />
                <rect x="17" y="14" width="2" height="1" fill="#c2bcb6" />
                <rect x="23" y="14" width="2" height="1" fill="#c2bcb6" />
                <rect x="12" y="15" width="12" height="1" fill="#c2bcb6" />
                <rect x="13" y="16" width="4" height="1" fill="#c2bcb6" />
                <rect x="19" y="16" width="4" height="1" fill="#c2bcb6" />
                <rect x="16" y="2" width="4" height="1" fill="#fdf6e7" />
                <rect x="14" y="3" width="8" height="1" fill="#fdf6e7" />
                <rect x="13" y="4" width="10" height="1" fill="#fdf6e7" />
                <rect x="9" y="5" width="18" height="1" fill="#fdf6e7" />
                <rect x="8" y="6" width="20" height="1" fill="#fdf6e7" />
                <rect x="8" y="7" width="20" height="1" fill="#fdf6e7" />
                <rect x="8" y="8" width="20" height="1" fill="#fdf6e7" />
                <rect x="8" y="9" width="20" height="1" fill="#fdf6e7" />
                <rect x="9" y="10" width="18" height="1" fill="#fdf6e7" />
                <rect x="10" y="11" width="16" height="1" fill="#fdf6e7" />
                <rect x="11" y="12" width="14" height="1" fill="#fdf6e7" />
                <rect x="12" y="13" width="12" height="1" fill="#fdf6e7" />
                <rect x="13" y="14" width="4" height="1" fill="#fdf6e7" />
                <rect x="19" y="14" width="4" height="1" fill="#fdf6e7" />
                <rect className="pensamiento__punto" x="13" y="9" width="2" height="2" fill="#3b444a" />
                <rect className="pensamiento__punto" x="17" y="9" width="2" height="2" fill="#3b444a" />
                <rect className="pensamiento__punto" x="21" y="9" width="2" height="2" fill="#3b444a" />
            </g>
        </svg>
    );
};
