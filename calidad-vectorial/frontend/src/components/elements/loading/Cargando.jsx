import { createPortal } from 'react-dom';
import './Cargando.css';

export const Cargando = ({ tamano = 40, texto = '', pantallaCompleta = false, className = '' }) => {
    const contenido = (
        <div
            className={`cargando ${pantallaCompleta ? 'cargando--pantalla' : ''} ${className}`}
            role="status"
            aria-live="polite"
        >
            <span
                className="cargando__icono"
                style={{ '--cargando-tamano': `${tamano}px` }}
                aria-hidden="true"
            />
            {texto ? <p className="cargando__texto">{texto}</p> : <span className="cargando__sr">Cargando</span>}
        </div>
    );

    return pantallaCompleta ? createPortal(contenido, document.body) : contenido;
};