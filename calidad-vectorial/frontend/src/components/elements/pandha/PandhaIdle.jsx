import sprite from '../../../assets/img/pandha/panda_idle.png';
import "./PandhaIlde.css";
 
/**
 * Idle del Pandha a partir de un sprite horizontal de 8 frames (360x288 c/u).
 *
 * @param {number}  width     Ancho en px (el alto se calcula, ratio 5:4).
 * @param {number}  duration  Duración de un loop completo en ms.
 * @param {boolean} paused    Congela la animación en el frame actual.
 */
export const PandhaIdle = ({ width = 300, duration = 2600, paused = false, className = '' }) => {
    return (
        <div
            className={`pandha-idle ${paused ? 'pandha-idle--paused' : ''} ${className}`}
            style={{
                '--pandha-width': `${width}px`,
                '--pandha-duration': `${duration}ms`,
                backgroundImage: `url(${sprite})`,
            }}
            role="img"
            aria-label="Pandha esperando"
        />
    );
};
 