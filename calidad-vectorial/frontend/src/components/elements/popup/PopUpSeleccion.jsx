import { createPortal } from 'react-dom';
import X from '../../../assets/img/icons/x.svg?react';
import { Button } from '../buttons/Button';
import './PopUp.css';

export const PopUpSeleccion = ({ foto, onClose, onSeleccionar, titulo }) => {
    const bloquearEvento = (e) => {
        e.stopPropagation();
    };
    return createPortal(
        <div className="popup"
            onClick={onClose}
        >
            <div className="popup__card popup__card--seleccion" onClick={(e) => e.stopPropagation()}>
                <div className="popup__card__text"
                    onMouseDown={bloquearEvento}
                    onMouseMove={bloquearEvento}
                    onMouseUp={bloquearEvento}
                    onTouchStart={bloquearEvento}
                    onTouchMove={bloquearEvento}
                    onTouchEnd={bloquearEvento}
                    onClick={bloquearEvento}>
                    <div>
                        <h2 className="popup__card__text__titulo">{titulo}</h2>
                    </div>
                <div className="popup__card__foto">
                    <img src={foto} alt="Foto" />
                </div>
                    <div className='popup__card__button'>
                        <Button onClick={onSeleccionar}>Seleccionar</Button>
                    </div>
                </div>
                <div className="popup__x" onClick={onClose}>
                    <X />
                </div>
            </div>
        </div>,
        document.body
    );
};
