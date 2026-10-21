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

export const CuadroZona = ({ predicciones, clase, tipo, confianza, tab, setTab, logueado }) => {
    const { data: dataZona , loading: loadingZona, error: errorZona, refetch: refetchZona } = useFetch(tipo && clase ? `${tipo}/nombre/${clase}` : null);

    const [referencia, setReferencia] = useState('');

    const zonaColor = dataZona?.zona_color?.toLowerCase();

    useEffect(() => {
        if (clase) refetchZona();
    }, [clase])

    return (
        <article className="mapa__cuadro contenedor">
            <header className={`mapa__cuadro__header mapa__cuadro__header--${loadingZona ? 'cargando' : ''} mapa__cuadro__header--${tab}`}>
                {!loadingZona && dataZona && tab === 'Info' && (
                    <h2>
                        {dataZona.tipo}
                        {dataZona.referencia && ` - ${dataZona.referencia}`}
                    </h2>
                )}
                <Pestanas
                    items={OPCIONES}
                    activa={tab}
                    onChange={setTab}
                    className='mapa__cuadro__header__pestanas'
                />
            </header>

            {loadingZona && logueado ? (
                <p>Cargando...</p>
            ) : dataZona ? (
                <div className="mapa__cuadro__panel">
                    {tab === 'Resultados' && (
                        predicciones ? (
                            <RenderResultados
                                predicciones={predicciones}
                            />
                        ) : (
                            <div className='mapa__cuadro__panel__galeria'>
                                <p>Carga una imagen en galeria para obtener una predicción</p>
                                <Button to='/galeria'>Galería</Button>
                            </div>
                        )
                    )}

                    {tab === 'Info' && (
                        !clase || loadingZona ? (
                            logueado ? (
                                <p>Selecciona una zona para ver</p>
                            ) : (
                                <div className='mapa__cuadro__data__login'>
                                    <p>Inicia sesión para ver los datos de las zonas</p>
                                    <Button to='/login'>Iniciar sesión</Button>
                                </div>
                            )
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
                                <Button to='/login'>Iniciar sesión</Button>
                            </div>
                        )
                    )}
                </div>
                ) : (
                    <p>No pudimos encontrar la zona</p>
            )}
        </article>
    );
}
