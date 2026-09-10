import { useLocation } from "react-router-dom";
import primerPiso from "../../../assets/img/floors/Primer-Piso.png";
import PulgarArriba from "../../../assets/img/icons/pulgarArriba.svg?react";
import PulgarAbajo from "../../../assets/img/icons/pulgarAbajo.svg?react";

import "./Mapa.css";

export const Mapa = () => {
    const location = useLocation();
    const resultado = location.state;

    return (
        <main className="mapa">
            <div className="mapa__img">
                <img src={primerPiso} alt="imagen del piso" width="800px" height="380px"/>
            </div>
            <div className="mapa__side">
                <article className="mapa__side__cuadro">
                    <div className="mapa__side__cuadro__data">
                        <h2>Aula</h2>
                        <p>Sector</p>
                        <p>Aula teórica</p>
                    </div>
                    <div className="mapa__side__cuadro__probabilidad">
                        <p>101% de probabilidades de que estés en esta aula</p>
                    </div>
                </article>
                
                <div className="mapa__side__opinion">
                    <p>¿La predicción fue correcta?</p>
                    <div className="mapa__side__opinion__svg"><PulgarArriba /></div>
                    <div className="mapa__side__opinion__svg"><PulgarAbajo /></div>
                </div>
            </div>
        </main>
    );
}