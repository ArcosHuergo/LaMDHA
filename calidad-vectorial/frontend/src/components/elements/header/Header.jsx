import { Link } from "react-router-dom";
import LaMDHA from "../../../assets/img/brand/lamdha.svg?react";
import Usuario from "../../../assets/img/icons/usuario.svg?react";

import "./Header.css"

export const Header = () => {
    return (
        <header className="header">
            <div>
                <Link to="/"><LaMDHA /></Link>
                <Link to="/">
                    LaMDHA
                </Link>
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