import { Link } from "react-router-dom";
import "./Button.css";

export const Button = ({children, type="button", variant="default", color="claro", to, isDisabled=false, onClick}) => {

    if (to && !isDisabled) {
        return (
            <Link to={to} className={`btn btn--${variant} btn--${variant}--${color}`}>
                {children}
            </Link>
        );
    }
    return (
        <button type={type} className={`btn btn--${variant} btn--${variant}--${isDisabled ? "disabled" : color}`} disabled={isDisabled} onClick={onClick}>{children}</button>
    );
}