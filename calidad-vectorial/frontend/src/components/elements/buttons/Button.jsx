import { Link } from "react-router-dom";
import Nube from "../../../assets/img/brand/Nube.svg?react"
import "./Button.css";

export const Button = ({children, type="button", variant="default", color="violeta", to, isDisabled=false, onClick}) => {

    if (to && !isDisabled) {
        return (
            <Link to={to} className={`btn btn--${variant} btn--${variant}--${color}`}>
                {children}
                {(variant == "subir" && (
                    <Nube />
                ))
                }
            </Link>
        );
    }
    return (
        <button type={type} className={`btn btn--${variant} btn--${variant}--${isDisabled ? "disabled" : color}`} disabled={isDisabled} onClick={onClick}>
            {children}
            {(variant == "subir" && (
                    <Nube />
                ))
                }
        </button>
    );
}