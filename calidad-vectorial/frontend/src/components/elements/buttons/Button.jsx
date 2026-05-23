import { Link } from "react-router-dom";
import "./Button.css";

export const Button = ({children, type="button", variant="solapa", color="claro", to, isDisabled=false, onClick}) => {

    if (to && !isDisabled) {
        if (variant == "solapa") {
            return (
                <Link to={to} className="btn">
                    <div className={`btn btn--${variant} btn--${variant}--${color}`}>
                        {children}
                    </div>
                    <span className={`btn btn--${variant} btn--${variant}--oscuro`}>
                        {children}
                    </span>
                </Link>
            );
        }
        return (
            <Link to={to} className={`btn btn--${variant} btn--${variant}--${color}`}>
                {children}
            </Link>
        );
    }

    if (variant == "solapa") {
        return (
            <button type={type} className={`btn btn--${variant} btn--${variant}--${isDisabled ? "disabled" : color}`} disabled={isDisabled} onClick={onClick}>
                <div className={`btn btn--${variant} btn--${variant}--${isDisabled ? "disabled" : color}`}>
                    {children}
                </div>
                <span className={`btn btn--${variant} btn--${variant}--oscuro`}>
                    {children}
                </span>
            </button>
        );
    }

    return (
        <button type={type} className={`btn btn--${variant} btn--${variant}--${isDisabled ? "disabled" : color}`} disabled={isDisabled} onClick={onClick}>{children}</button>
    );
}