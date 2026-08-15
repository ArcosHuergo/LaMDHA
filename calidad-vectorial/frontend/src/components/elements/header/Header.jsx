import LaMDHA from "../../../assets/img/brand/lamdha.svg?react";
import Usuario from "../../../assets/img/brand/usuario.svg?react";

import "./Header.css"

export const Header = () => {
    return (
        <header className="header">
            <div>
                <LaMDHA />
                <p>
                    LaMDHA
                </p>
            </div>
            <div>
                <Usuario />
                <p>
                    Usuario
                </p>
                

            </div>
            
        </header>
    );
}