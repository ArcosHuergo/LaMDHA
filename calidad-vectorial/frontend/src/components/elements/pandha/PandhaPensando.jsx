import sprite from '../../../assets/img/pandha/panda_idle.png';
import { Pensamiento } from './Pensamiento';
import './PandhaPensando.css';

/**
 * Pandha pensando: usa el mismo sprite que PandhaIdle pero solo los frames de parpadeo
 * (sin suspiro ni respiración) y le suma la burbuja de pensamiento sobre la cabeza.
 *
 * @param {number} width  Ancho del panda en px (la burbuja escala con él).
 */
export const PandhaPensando = ({ width = 260, className = '' }) => {
    return (
        <div
            className={`pandha-pensando ${className}`}
            style={{ '--pandha-width': `${width}px` }}
            role="img"
            aria-label="Pandha pensando"
        >
            <div
                className="pandha-pensando__sprite"
                style={{ backgroundImage: `url(${sprite})` }}
            />
            <div className="pandha-pensando__burbuja">
                <Pensamiento />
            </div>
        </div>
    );
};
