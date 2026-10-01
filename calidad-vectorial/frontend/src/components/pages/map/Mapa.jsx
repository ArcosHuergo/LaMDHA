import { useState, useEffect } from "react";
import { useLocation } from "react-router-dom";

import { usePost } from '../../utils/fetch/FetchUtils';

import PulgarArriba from '../../../assets/img/icons/pulgarArriba.svg?react';
import PulgarAbajo from '../../../assets/img/icons/pulgarAbajo.svg?react';

import { PlanoPiso } from "../../elements/floor/PlanoPiso";
import { FachadaPisos } from "../../elements/floor/FachadaPisos";
import { AscensorPisos } from "../../elements/floor/AscensorPisos";
import { CuadroZona } from "../../elements/map/CuadroZona";

import { Button } from '../../elements/buttons/Button';

import './Mapa.css';

export const Mapa = () => {
    const location = useLocation();
    const resultado = location.state;

    const predicciones = resultado ? resultado.predicciones : undefined;
    const id = resultado ? resultado.registro_id : undefined;
    const piso = resultado ? resultado.piso : undefined;
    const zona = resultado ? resultado.predicciones[0].clase : undefined

    const [pisoActual, setPisoActual] = useState(piso);
    const [zonaSeleccionada, setZonaSeleccionada] = useState(zona);

    const confianzaSeleccionada = zonaSeleccionada
        ? predicciones?.find((p) => p.clase === zonaSeleccionada.className)?.confianza ?? null : null;

    const { loading, error, execute } = usePost(`registrofeedback/${id}`, "PATCH");

    const [enviando, setEnviando] = useState(false);
    const activarOpinion = enviando ? "not-allowed" : "pointer"
    const handle_opinion = async (event) => {
        if (enviando) return;
        setEnviando(true);

        try {
            const resultado = await execute({
                prediccion_correcta: event.currentTarget.value
            });

            await new Promise(resolve => setTimeout(resolve, 2000));
        } finally {
            setEnviando(false);
        }
    };

    return (
        <main className="mapa">
            <div className="mapa__izq">
                <div className="mapa__izq__img">
                    <PlanoPiso
                        piso={pisoActual}
                        predicciones={predicciones}
                        zonaSeleccionada={zonaSeleccionada}
                        onZonaClick={setZonaSeleccionada}
                    />
                </div>
                <div className="mapa__izq__button">
                    <Button to="/galeria">{'← Volver'}</Button>
                </div>

            </div>
            <div className="mapa__side">
                <CuadroZona
                    className={zonaSeleccionada?.className}
                    tipo={zonaSeleccionada?.tipo}
                    confianza={confianzaSeleccionada}
                />
            </div>

            <div className="mapa__fachada">
                <FachadaPisos pisoActual={pisoActual} onClick={setPisoActual}/>
            </div>

            <div className="mapa__opinion">
                <div className="mapa__side__opinion">
                    <p>¿La predicción fue correcta?</p>
                    <div className="mapa__opinion__botones">
                        {id != null ? (
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
                        {id != null ? (
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
            </div>
        </main>
    );
};
