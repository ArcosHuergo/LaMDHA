import { useEffect } from 'react';
import { useFetch, usePost } from '../../utils/fetch/FetchUtils';

import "./CuadroZona.css";

export const CuadroZona = ({ className, tipo, confianza }) => {
    const { data, loading, error, refetch } = useFetch(tipo && className ? `${tipo}/nombre/${className}` : null);

    useEffect(() => {
        if (className) refetch();
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

    if (loading) {
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
                <h2>{data.nombre}</h2>
                <p>Referencia {data.referencia}</p>
                <p>{data.descripcion}</p>
            </div>
            {confianza != null && confianza != undefined && (
                <div className="mapa__cuadro__probabilidad">
                    <p>{Math.round(confianza * 100)}% de probabilidades de que estés en esta aula</p>
                </div>
            )}
        </article>
    )
}