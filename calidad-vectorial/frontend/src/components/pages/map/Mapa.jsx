import { useLocation } from "react-router-dom";
import primerPiso from "../../../assets/img/floors/Primer-Piso.png";

import "./Mapa.css";

export const Mapa = () => {
    const location = useLocation();
    const resultado = location.state;

    return (
        <main className="mapa">
            <div className="mapa__img">
                <img src={primerPiso} alt="imagen del piso" width="800px" height="380px"/>
            </div>
            <article className="mapa__cuadro">
                <div>
                    <h2>Aula</h2>
                    <p>Sector</p>
                    <p>Aula teórica</p>
                </div>
                <div>
                    <p>Probabilidad de %</p>
                </div>
            </article>
        </main>
    );
}