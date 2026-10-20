import { useState, useEffect } from "react";
import { useLocation } from "react-router-dom";

import { useFetch, usePost } from '../../utils/fetch/FetchUtils';

import PulgarArriba from '../../../assets/img/icons/pulgarArriba.svg?react';
import PulgarAbajo from '../../../assets/img/icons/pulgarAbajo.svg?react';

import { PlanoPiso } from "../../elements/floor/PlanoPiso";
import { FachadaPisos } from "../../elements/floor/FachadaPisos";
import { CuadroZona } from "../../elements/map/CuadroZona";
import { Pestanas } from "../../elements/tab/Pestanas";

import { Button } from '../../elements/buttons/Button';

import './Mapa.css';

const PISOS = [
    { id: 'PB', nombre: 'Planta Baja' },
    { id: 'EPB', nombre: 'Entrepiso PB' },
    { id: 'P1', nombre: 'Primer Piso' },
    { id: 'EP1', nombre: 'Entrepiso P1' },
    { id: 'P2', nombre: 'Segundo Piso' },
    { id: 'P3', nombre: 'Tercer Piso' },
];

export const Mapa = () => {
    const location = useLocation();
    const resultado = location.state;

    const imagenUrl = resultado ? resultado.imagenUrl : undefined;

    const predicciones = resultado ? resultado.predicciones : undefined;
    const id = resultado ? resultado.registro_id : undefined;
    const piso = resultado ? resultado.piso : 'PB';
    const zona = resultado ? resultado.predicciones[0].clase : undefined

    const [pisoActual, setPisoActual] = useState(piso);
    const [zonaSeleccionada, setZonaSeleccionada] = useState(zona);
    const [referencia, setReferencia] = useState('');

    const confianzaSeleccionada = zonaSeleccionada
        ? predicciones?.find((p) => p.clase === zonaSeleccionada.className)?.confianza ?? null : null;

    const { execute: executeFeedback } = usePost(`registro/feedback/${id}`, "PATCH");

    const { data: dataUsuario, error: errorToken } = useFetch('auth/validar-token');

    const [enviando, setEnviando] = useState(false);
    const activarOpinion = enviando ? "not-allowed" : "pointer"
    const handle_opinion = async (event) => {
        if (enviando) return;
        setEnviando(true);

        try {
            const resultado = await executeFeedback({
                prediccion_correcta: event.currentTarget.value
            });

            await new Promise(resolve => setTimeout(resolve, 2000));
        } finally {
            setEnviando(false);
        }
    };

    return (
        <main className="mapa">
            <header className="mapa__header">
                <Button to='/galeria'>{'← volver'}</Button>
                {referencia ? (
                    <h1>Estás en {referencia[1]} {referencia[0]}</h1>
                ) : (
                    <h1>Estás en {zona}</h1>
                )}
            </header>
            <section className="mapa__plano contenedor">
                <header className="mapa__plano__header">
                    <h2 className="mapa__plano__titulo">
                        {PISOS.find((p) => p.id === pisoActual)?.nombre}
                    </h2>
                    <Pestanas
                        items={PISOS}
                        activa={pisoActual}
                        onChange={setPisoActual}
                    />
                </header>

                <div className="mapa__plano__img">
                    <PlanoPiso
                        piso={pisoActual}
                        predicciones={predicciones}
                        zonaSeleccionada={zonaSeleccionada}
                        onZonaClick={setZonaSeleccionada}
                    />
                </div>

                <footer className="mapa__plano__leyenda">
                    <span>Menos probable</span>
                    <div className="mapa__plano__barra" />
                    <span>Más probable</span>
                </footer>
            </section>

            <section className="mapa__side">
                <div className="mapa__side__img contenedor">
                    <img src={imagenUrl} alt="Imagen ingresada" />
                    <span>TU FOTO</span>
                </div>
                <CuadroZona
                    predicciones={predicciones}
                    clase={zonaSeleccionada?.className}
                    tipo={zonaSeleccionada?.tipo}
                    confianza={confianzaSeleccionada}
                    referencia={referencia}
                    setReferencia={setReferencia}
                    logueado={errorToken ? false : true}
                />
            </section>

            {/* <div className="mapa__fachada">
                <FachadaPisos pisoActual={pisoActual} onClick={setPisoActual}/>
            </div> */}

            {/* <div className="mapa__opinion">
                <div className="mapa__side__opinion">
                    <p>¿La predicción fue correcta?</p>
                    <div className="mapa__opinion__botones">
                        {id ? (
                            <button className="mapa__opinion__svg"
                                onClick={handle_opinion}
                                value={true}
                                style={{ cursor: activarOpinion }}
                            >
                                <PulgarArriba />
                            </button>
                        ) : (
                            <div className="mapa__opinion__svg">
                                <PulgarArriba />
                            </div>
                        )}
                        {id ? (
                            <button className="mapa__opinion__svg"
                                onClick={handle_opinion}
                                value={false}
                                style={{ cursor: activarOpinion }}
                            >
                                <PulgarAbajo />
                            </button>
                        ) : (
                            <div className="mapa__opinion__svg">
                                <PulgarAbajo />
                            </div>
                        )}
                    </div>
                </div>
            </div> */}
        </main>
    );
};
