import pasto from '../../../assets/img/pandha/pasto.png';
import './Pasto.css';

/**
 * Franja de pasto que ondea con el viento.
 * Se corta en segmentos angostos; cada uno se mece con un pequeño desfase
 * respecto al anterior, así la "ola" recorre el pasto de izquierda a derecha.
 *
 * @param {number} segmentos  Cantidad de segmentos (cubre segmentos * 48px de ancho).
 * @param {number} alto       Alto de la franja en px.
 */
export const Pasto = ({ segmentos = 32, alto = 40, className = '' }) => {
    return (
        <div
            className={`pasto ${className}`}
            style={{ '--pasto-img': `url(${pasto})`, '--pasto-alto': `${alto}px` }}
            aria-hidden="true"
        >
            {/* capa de atrás: más oscura y desplazada, da profundidad */}
            <div className="pasto__capa pasto__capa--atras">
                {Array.from({ length: segmentos }, (_, i) => (
                    <span key={i} className="pasto__seg" style={{ '--i': i }} />
                ))}
            </div>
            <div className="pasto__capa pasto__capa--frente">
                {Array.from({ length: segmentos }, (_, i) => (
                    <span key={i} className="pasto__seg" style={{ '--i': i }} />
                ))}
            </div>
        </div>
    );
};
