import { useEffect, useRef } from "react";
import "./OjosAnimados.css";

export const OjosAnimados = () => {
    // Referencias a los elementos DOM de los ojos y pupilas
    const ojoRef = useRef(null);
    const pupilaRef = useRef(null);
    const ojoRef2 = useRef(null);
    const pupilaRef2 = useRef(null);
    const parpadeoBloqueadoRef = useRef(false);

    // Estado para controlar si los ojos están cerrados
    const ojosCerradosRef = useRef(false);

    // Referencia para manejar el ciclo de animación
    const animacionFrameRef = useRef(null);

    useEffect(() => {
        const ojo1 = ojoRef.current;
        const pupila1 = pupilaRef.current;
        const ojo2 = ojoRef2.current;
        const pupila2 = pupilaRef2.current;

        // Si no se encuentran los elementos, no se ejecuta la lógica
        if (!ojo1 || !pupila1 || !ojo2 || !pupila2) return;

        let mouseX = 0;
        let mouseY = 0;

        // Actualiza la posición del mouse
        const manejarMovimientoMouse = (e) => {
            mouseX = e.clientX;
            mouseY = e.clientY;
        };

        /**
         * Mueve la pupila dentro del ojo en dirección al cursor
         * @param {HTMLElement} ojo - Elemento del ojo
         * @param {HTMLElement} pupila - Elemento de la pupila
         */
        const actualizarPupila = (ojo, pupila) => {
            if (!ojo || !pupila) return;

            const rect = ojo.getBoundingClientRect();
            const centroOjoX = rect.left + rect.width / 2;
            const centroOjoY = rect.top + rect.height / 2;

            const dx = mouseX - centroOjoX;
            const dy = mouseY - centroOjoY;
            const angulo = Math.atan2(dy, dx);
            const distancia = Math.sqrt(dx * dx + dy * dy);

            const movimientoMaximo = 10;
            const movimiento = Math.min(movimientoMaximo, distancia / 20);

            // Solo mueve la pupila si el ojo está abierto
            if (!ojo.classList.contains("rostro__ojo--cerrado")) {
                const offsetCentro = 13;
                pupila.style.left = offsetCentro + movimiento * Math.cos(angulo) + "px";
                pupila.style.top = offsetCentro + movimiento * Math.sin(angulo) + "px";
            }
        };

        // Actualiza ambos ojos en cada frame de animación
        const actualizarOjos = () => {
            actualizarPupila(ojo1, pupila1);
            actualizarPupila(ojo2, pupila2);
            animacionFrameRef.current = requestAnimationFrame(actualizarOjos);
        };

        // Simula un parpadeo cerrando y abriendo los ojos brevemente
        const parpadear = () => {
            if (ojosCerradosRef.current || parpadeoBloqueadoRef.current) return;
            ojo1.classList.add("rostro__ojo--cerrado");
            ojo2.classList.add("rostro__ojo--cerrado");
            setTimeout(() => {
                // Chequea si los ojos deben permanecer cerrados
                if (!ojosCerradosRef.current && !parpadeoBloqueadoRef.current) {
                    ojo1.classList.remove("rostro__ojo--cerrado");
                    ojo2.classList.remove("rostro__ojo--cerrado");
                }
            }, 150);
        };

        // Intervalo aleatorio para parpadear cada 3 a 5 segundos
        const intervaloParpadeo = setInterval(parpadear, 3000 + Math.random() * 2000);

        // Cierra los ojos al enfocar un campo de contraseña
        const manejarFocoPassword = () => {
            parpadeoBloqueadoRef.current = true;
            ojosCerradosRef.current = true;
            ojo1.classList.add("rostro__ojo--cerrado");
            ojo2.classList.add("rostro__ojo--cerrado");
        };

        // Abre los ojos al perder el foco del campo de contraseña
        const manejarBlurPassword = () => {
            // Desbloquea el parpadeo cuando se deja de seleccionar el input
            parpadeoBloqueadoRef.current = false;
            ojosCerradosRef.current = false;

            ojo1.classList.remove("rostro__ojo--cerrado");
            ojo2.classList.remove("rostro__ojo--cerrado");
        };

        //Abre un ojo cuando se muestra la contraseña
        const manejarEspiarPassword = () => {
            //Bloquea el parpadeo
            parpadeoBloqueadoRef.current = true;
            ojo1.classList.add("rostro__ojo--cerrado");
            ojo2.classList.add("rostro__ojo--cerrado");
            // Probabilidad de chusmear (50% de probabilidad)
            const probChusmear = Math.random();
            // Probabilidad de abrir cada ojo (50% de probabilidad)
            const probOjo = Math.random();

            if (probChusmear  < 0.5) {
                if (probOjo < 0.5) {
                    ojo1.classList.remove("rostro__ojo--cerrado");
                    ojo2.classList.add("rostro__ojo--cerrado");
                } else {
                    ojo1.classList.add("rostro__ojo--cerrado");
                    ojo2.classList.remove("rostro__ojo--cerrado");
                }
            }
        };


        // Listeners para movimiento del mouse y eventos personalizados
        window.addEventListener("passwordPeek", manejarEspiarPassword);
        window.addEventListener("mousemove", manejarMovimientoMouse);
        window.addEventListener("passwordFocus", manejarFocoPassword);
        window.addEventListener("passwordBlur", manejarBlurPassword);

        // Inicia la animación de seguimiento ocular
        animacionFrameRef.current = requestAnimationFrame(actualizarOjos);

        // Limpieza al desmontar el componente
        return () => {
            clearInterval(intervaloParpadeo);
            if (animacionFrameRef.current) {
                cancelAnimationFrame(animacionFrameRef.current);
            }
            window.removeEventListener("passwordPeek", manejarEspiarPassword);
            window.removeEventListener("mousemove", manejarMovimientoMouse);
            window.removeEventListener("passwordFocus", manejarFocoPassword);
            window.removeEventListener("passwordBlur", manejarBlurPassword);
        };
    }, []);

    return (
        <div className="rostro__ojos">
            <div className="rostro__ojo rostro__ojo--izquierdo" ref={ojoRef}>
                <div className="rostro__pupila" ref={pupilaRef}></div>
                <div className="rostro__parpado"></div>
            </div>
            <div className="rostro__ojo rostro__ojo--derecho" ref={ojoRef2}>
                <div className="rostro__pupila" ref={pupilaRef2}></div>
                <div className="rostro__parpado"></div>
            </div>
        </div>
    );
};