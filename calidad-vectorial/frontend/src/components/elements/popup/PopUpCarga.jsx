import Pandha from "../../../assets/img/pandha/pandha.svg?react";
import Nube from "../../../assets/img/pandha/nube.svg?react";
import Nubecita from "../../../assets/img/pandha/nubecita.svg?react";
import { Bamboos } from "./Bamboos";

import "./PopUp.css"

export const PopUpCarga = () => {
    return (
        <div className="popup">
            <div className="popup__card" onClick={(e) => e.stopPropagation()}>
                <div className="pop__card__carga">
                    <p>Estamos procesando tu imagen...</p>
                    <div className="pop__card__carga__mascota">
                        <div className="pop__card__carga__mascota__nube">
                            <Nube />
                        </div>
                        <div className="pop__card__carga__mascota__nubecita--uno">
                            <Nubecita />
                        </div>
                        <div className="pop__card__carga__mascota__nubecita--dos">
                            <Nubecita />
                        </div>
                        <div className="pop__card__carga__mascota__pandha">
                            <Pandha />
                        </div>
                        <div className="pop__card__carga__mascota__bamboos">
                            <Bamboos />
                        </div>
                    </div>
                </div>
            </div>
        </div>
    );
};
