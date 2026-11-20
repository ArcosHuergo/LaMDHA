import { Cargando } from '../loading/Cargando';
import './RenderInfo.css';

export const RenderInfo = ({ zonaColor, descripcion, imagenUrl, loadingFoto, errorFoto, nombre }) => {
    return (
        <div className="info">
            {loadingFoto ? (
                <Cargando className='info__img' texto='Cargando imagen' />
            ) : !errorFoto ? (
                <img
                    className='info__img'
                    src={imagenUrl}
                    alt={`Foto de referencia de ${nombre}`}
                />
            ) : (
                <div className='info__img info__error'>
                    <p>Foto no encontrada</p>
                </div>
            )}
            
            <div className="info__text">
                <p>{zonaColor && `Sector ${zonaColor}`}</p>
                <p>{descripcion}</p>
            </div>
            
        </div>
    )
}
