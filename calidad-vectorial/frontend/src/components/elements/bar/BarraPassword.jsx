import { validarSeguridadPassword } from "../../utils/LoginUtils";
import "./BarraPassword.css";

export const BarraPassword = ({ password }) => {
    const seguridad = validarSeguridadPassword(password);
    const progreso = seguridad * 100 / 5;

    const colores = ["#ff4d4f", "#ff7a45", "#ffa940", "#73d13d", "#389e0d"];
    const color = colores[seguridad - 1];

    return (
        <div className="div-password">
            
            <span className="div-password__span">Nivel de seguridad:</span>
            <p className={`div-password__texto div-password__texto--${!seguridad ? "no-mostrar" : ""}`}
                style={{color: color}}>
                {seguridad === 5 ? "Muy fuerte"
                : seguridad === 4 ? "Fuerte"
                : seguridad === 3 ? "Medio"
                : seguridad === 2 ? "Débil"
                : "Muy débil"
            }</p>
            <div className="div-password__barra">
                <div className={`div-password__barra__color`} style={{width:`${progreso}%`, backgroundColor: color}}></div>
            </div>
        </div>
    );
};