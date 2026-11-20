import { Cargando } from '../loading/Cargando';
import './RenderReferencia.css';

export const RenderReferencia = ({ imagenUrl, loading, error, nombre }) => {
    if (loading) {
        return (
            <div className="referencia">
                <Cargando />
            </div>
        );
    }

    if (error || !imagenUrl) {
        return (
            <div className="referencia">
                <p>Foto no encontrada</p>
            </div>
        );
    }

    return (
        <div className="referencia">
            <img
                className="referencia__img"
                src={imagenUrl}
                alt={`Foto de referencia de ${nombre}`}
            />
        </div>
    );
};