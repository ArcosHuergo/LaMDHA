import { useState, useRef } from "react"
import "./Input.css";

export const Input = ({ children, type="text", name, value, checked, placeholder, variant="default", title, required=true, disabled=false, onChange, onFocus, onBlur , autoComplete="off", autoCorrect="off", autoCapitalize="none", spellCheck="false"}) => {
    const [showPassword, setShowPassword] = useState(false);
    const inputRef = useRef(null);

    const togglePassword = (e) => {
        e.preventDefault();
        setShowPassword((inputType) => !inputType);

        if (inputRef.current) {
            // Selecciona el input si se toca el ojo
            inputRef.current.focus();
        }

            if (inputType === "password") {
                // Chusmea la contraseña
                window.dispatchEvent(new Event("passwordPeek"));
            }
            if (inputType === "text") {
                // Cierra los ojos
                window.dispatchEvent(new Event("passwordFocus"));
            }
    };

    const inputType = type == "password" && showPassword ? "text" : type;

    return (
        <input className="input" type={type} placeholder={placeholder}/>
    );
};