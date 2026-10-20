import { useEffect, useState } from 'react';
import { useFetch, usePost } from '../../utils/fetch/FetchUtils';
import { RenderInfo } from './RenderInfo';
import { RenderResultados } from './RenderResultados';
import { Pestanas } from '../tab/Pestanas';
import { Button } from '../buttons/Button';

import "./CuadroZona.css";

const OPCIONES = [
    { id: 'Resultados', nombre: 'Resultados' },
    { id: 'Info', nombre: 'Info' },
]

export const CuadroZona = ({ predicciones, clase, tipo, confianza, referencia, setReferencia, logueado }) => {
    const { data: dataZona , loading: loadingZona, error: errorZona, refetch: refetchZona } = useFetch(tipo && clase ? `${tipo}/nombre/${clase}` : null);

    const [tab, setTab] = useState('Resultados');

    const zonaColor = dataZona?.zona_color?.toLowerCase();
    if (dataZona && dataZona.referencia && dataZona.tipo && referencia === '') {
        if (dataZona.referencia != dataZona.tipo) setReferencia([dataZona.referencia, dataZona.tipo]);
        else setReferencia([dataZona.referencia]);
    };

    useEffect(() => {
        if (clase) refetchZona();
    }, [clase])

    return (
        <article className="mapa__cuadro contenedor">
            <header className={`mapa__cuadro__header mapa__cuadro__header--${tab}`}>
                {tab === 'Info' && (
                    <h2>
                        {dataZona.tipo}
                        {dataZona.referencia && ` - ${dataZona.referencia}`}
                    </h2>
                )}
                <Pestanas
                    items={OPCIONES}
                    activa={tab}
                    onChange={setTab}
                />
            </header>

            <div className="mapa__cuadro__panel">
                {tab === 'Resultados' && (
                    <RenderResultados
                        predicciones={predicciones}
                    />
                )}

                {tab === 'Info' && (
                    !clase || loadingZona ? (
                        <div className="mapa__cuadro__data">
                            <p>Selecciona una zona para ver</p>
                        </div>
                    ) : logueado ? (
                        <div className="mapa__cuadro__data">
                            <div className="mapa__cuadro__data__text">
                                <p>{zonaColor && `Sector ${zonaColor}`}</p>
                                <p>{dataZona.descripcion}</p>
                            </div>
                        </div>
                    ) : (
                        <div className='mapa__cuadro__data__login'>
                            <p>Inicia sesión para ver los datos de las zonas</p>
                            <Button to='/login'>iniciar sesión</Button>
                        </div>
                        
                    )
                )}
            </div>
        </article>
    );
}
