import { Link } from "react-router-dom";
import Upload from "../../../assets/img/icons/upload.svg?react"
import "./Button.css";

export const Button = ({
    children,
    type = "button",
    variant = "default",
    color = "violeta",
    to,
    isDisabled = false,
    onClick,
    file,
    onFileChange
}) => {

    if (variant === "subir") {
        const handleFileChange = (e) => {
            const selectedFile = e.target.files?.[0];
            if (selectedFile && onFileChange) {
                onFileChange(selectedFile);
            }
            // Permite volver a seleccionar el mismo archivo si hace falta
            e.target.value = "";
        };

        return (
            <div className="btn-subir-group">
                <label className={`btn btn--subir btn--subir--${color}`}>
                    {file && (
                        <span className="btn--subir__filename">{file.name}</span>
                    )}
                    {children}
                    <input
                        type="file"
                        accept=".jpg,.jpeg,image/jpeg"
                        onChange={handleFileChange}
                        hidden
                    />
                </label>

                <button
                    type="button"
                    className={`btn btn--enviar btn--enviar--${color}`}
                    disabled={!file}
                    onClick={onClick}
                    title="enviar"
                >
                    <Upload />
                </button>
            </div>
        );
    }

    if (to && !isDisabled) {
        return (
            <Link to={to} className={`btn btn--${variant} btn--${variant}--${color}`}>
                {children}
            </Link>
        );
    }
    return (
        <button type={type} className={`btn btn--${variant} btn--${variant}--${color} btn--${isDisabled ? "disabled" : color}`} disabled={isDisabled} onClick={onClick}>
            {children}
        </button>
    );
}