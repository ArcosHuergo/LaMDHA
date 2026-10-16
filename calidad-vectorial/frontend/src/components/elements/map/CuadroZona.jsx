import { useEffect } from 'react';
import { useFetch, usePost } from '../../utils/fetch/FetchUtils';

import "./CuadroZona.css";

export const CuadroZona = ({ className, tipo, confianza, src, alt }) => {
    const { data: dataZona , loading: loadingZona, error: errorZona, refetch: refetchZona } = useFetch(tipo && className ? `${tipo}/nombre/${className}` : null);

    const zonaColor = dataZona?.zona_color?.toLowerCase();

    useEffect(() => {
        if (className) refetchZona();
    }, [className])

    if (!className) {
        return (
            <article className="mapa__cuadro">
                <div className="mapa__cuadro__data">
                    <p>Selecciona una zona para ver</p>
                </div>
            </article>
        );
    }

    if (loadingZona) {
        return(
            <article className="mapa__cuadro">
                <div className="mapa__cuadro__data">
                    <p>Cargando...</p>
                </div>
            </article>
        );
    }

    return (
        <article className="mapa__cuadro">
            <div className="mapa__cuadro__data">
                <div className='mapa__cuadro__data__text'>
                    <h2>{dataZona.tipo} {dataZona.referencia ? '- ' + dataZona.referencia : ''}</h2>
                    <p>Sector {zonaColor}</p>
                    <p>{dataZona.descripcion}</p>
                </div>
                <img src={src} alt={alt} />
            </div>
            {confianza != null && confianza != undefined && (
                <div className="mapa__cuadro__probabilidad">
                    <p>{Math.round(confianza * 100)}% de probabilidades de que estés en esta aula</p>
                </div>
            )}
        </article>
    )
}