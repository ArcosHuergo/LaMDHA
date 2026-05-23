import { useState, useRef } from "react"
import "./Input.css";
import ver from "../../../assets/img/ver.png";
import esconder from "../../../assets/img/esconder.png";

export const Input = ({ children, type, name, value, checked, placeholder, variant="default", title, required=true, disabled=false, onChange, onFocus, onBlur , autoComplete="off", autoCorrect="off", autoCapitalize="none", spellCheck="false"}) => {
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

    if (variant == "grande") {
        return (
            <div className="input-group">
                <textarea className={`input-group__input input-group__input--${type} input-group__input--${variant}`} placeholder={placeholder} title={title} onChange={onChange} ref={inputRef}
                onFocus={() => {
                    if (type == "password") {if (inputType === "text") {window.dispatchEvent(new Event("passwordPeek"));} else {window.dispatchEvent(new Event("passwordFocus"))};}
                }}
                onBlur={ () => {
                    if (type == "password") {window.dispatchEvent(new Event("passwordBlur"))}}}
                name={name} id={name} type={inputType} value={value ?? ""} required={required} disabled={disabled} />

                <label className="input-group__label" htmlFor={name}> {children} </label>

                {type === "password" && (
                    <button type="button" className="input-group__ojo" onMouseDown={togglePassword}  >

                        {showPassword ? (
                            <img src={esconder} alt="esconder" />
                        ): (
                            <img src={ver} alt="ver" />
                        )}
                    </button>
                )}
            </div>
        );
    };

    if (variant == "medio") {
        return(
            <div className="input-group">
                <textarea className={`input-group__input input-group__input--${type} input-group__input--${variant}`} placeholder={placeholder} title={title} onChange={onChange} ref={inputRef}
                onFocus={() => {
                    if (type == "password") {if (inputType === "text") {window.dispatchEvent(new Event("passwordPeek"));} 
                    else {window.dispatchEvent(new Event("passwordFocus"))};}
                }}
                onBlur={ () => {
                    if (type == "password") {window.dispatchEvent(new Event("passwordBlur"))}}}
                name={name} id={name} type={inputType} value={value ?? ""} required={required} disabled={disabled} />
                <label className="input-group__label" htmlFor={name}> {children} </label>

                {type === "password" && (
                    <button type="button" className="input-group__ojo" onMouseDown={togglePassword}  >
                        {showPassword ? (
                            <img src={esconder} alt="esconder" />
                        ): (
                            <img src={ver} alt="ver" />
                        )}
                    </button>
                )}
            </div>
        );
    };

    if (type == "checkbox") {
        return (
            <div className="input-group input-group--checkbox">
                <span className="input-group--checkbox__text" htmlFor={name}>{children}</span>
                <input className={`input-group__input--${type}`} type="checkbox" placeholder={placeholder} title={title} onChange={onChange} ref={inputRef}
                name={name} id={name} checked={checked ?? ""} required={false} disabled={disabled}
                autoComplete={autoComplete} autoCorrect={autoCorrect} autoCapitalize={autoCapitalize} spellCheck={spellCheck}/>
            </div>
        );
    };

    return (
        <div className="input-group">
            <input className={`input-group__input input-group__input--${type} input-group__input--${variant}`} placeholder={placeholder} title={title} onChange={onChange} ref={inputRef}
            onFocus={() => {
                if (type == "password") {if (inputType === "text") {window.dispatchEvent(new Event("passwordPeek"));}
                else {window.dispatchEvent(new Event("passwordFocus"))};}
                else {onFocus && onFocus()}
            }}
            onBlur={ () => {
                if (type == "password") {window.dispatchEvent(new Event("passwordBlur"))}
                else {onBlur && onBlur()}}}
            name={name} id={name} type={inputType} value={value ?? ""} required={required} disabled={disabled}
            autoComplete={autoComplete} autoCorrect={autoCorrect} autoCapitalize={autoCapitalize} spellCheck={spellCheck}/>

            <label className="input-group__label" htmlFor={name}> {children} </label>

            {type === "password" && (
                <button type="button" className="input-group__ojo" onMouseDown={togglePassword}  >
                    {showPassword ? (
                        <img src={esconder} alt="esconder" />
                    ): (
                        <img src={ver} alt="ver" />
                    )}
                </button>
            )}
        </div>
    );
};