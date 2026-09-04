import X from "../../../assets/img/icons/x.svg?react";
import { Button } from "../buttons/Button";
import "./Popup.css";

export const PopUpSeleccion = ({ children, foto, onClose, onSeleccionar, titulo }) => {
    const bloquearEvento = (e) => {
        e.stopPropagation();
    };
    return (
        <div className="popup" onClick={onClose}>
            <div className="popup__card" onClick={(e) => e.stopPropagation()}>
                <div className="popup__card__foto"
                    onMouseDown={bloquearEvento}
                    onMouseMove={bloquearEvento}
                    onMouseUp={bloquearEvento}
                    onTouchStart={bloquearEvento}
                    onTouchMove={bloquearEvento}
                    onTouchEnd={bloquearEvento}
                    onClick={bloquearEvento}
                >
                    <img src={foto} alt="Foto" />
                </div>
                <div className="popup__card__text">
                    <div>
                        <h2 className="popup__card__text__titulo">{titulo}</h2>
                        <p className="popup__card__text__descripcion">{children}</p>
                    </div>
                    <div>
                        <Button onClick={onSeleccionar}>Seleccionar</Button>
                    </div>
                </div>
                <div className="popup__x" onClick={onClose}>
                    <X />
                </div>
            </div>
        </div>
    );
}