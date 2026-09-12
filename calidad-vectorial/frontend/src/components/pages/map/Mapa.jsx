import { useState } from "react";
import { useLocation } from "react-router-dom";

import PulgarArriba from "../../../assets/img/icons/pulgarArriba.svg?react";
import PulgarAbajo from "../../../assets/img/icons/pulgarAbajo.svg?react";

import { PlanoPiso } from "../../elements/floor/PlanoPiso";
import { pisos } from "../../data/pisos";

import "./Mapa.css";

export const Mapa = () => {
    const location = useLocation();
    const resultado = location.state;

    const confianza = resultado.predicciones[0].confianza * 100;

    const [pisoActual, setPisoActual] = useState("P1");

    return (
        <main className="mapa">
            <div className="mapa__img">
                <PlanoPiso piso={pisoActual} predicciones={resultado.predicciones}/>
            </div>
            <div className="mapa__side">
                <article className="mapa__side__cuadro">
                    <div className="mapa__side__cuadro__data">
                        <h2>Aula</h2>
                        <p>Sector</p>
                        <p>Aula teórica</p>
                    </div>
                    <div className="mapa__side__cuadro__probabilidad">
                        <p>{confianza}% de probabilidades de que estés en esta aula</p>
                    </div>
                </article>
                
                <div className="mapa__side__opinion">
                    <p>¿La predicción fue correcta?</p>
                    <div className="mapa__side__opinion__botones">
                        <div className="mapa__side__opinion__svg"><PulgarArriba /></div>
                        <div className="mapa__side__opinion__svg"><PulgarAbajo /></div>
                    </div>
                </div>
            </div>
            <div className="mapa__seleccion">
                {Object.keys(pisos).map((key) => (
                    <button
                        key={key}
                        onClick={() => setPisoActual(key)}
                        disabled={key === pisoActual}
                    >
                        {key}
                    </button>
                ))}
            </div>
        </main>
    );
}