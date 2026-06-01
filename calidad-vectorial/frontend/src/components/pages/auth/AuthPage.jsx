import { useState } from "react";
import { useNavigate, Link, useLocation  } from "react-router-dom";
import { FondoFachero } from "../../elements/prettybackground/FondoFachero"
import { AuthBox } from "../../elements/authbox/AuthBox";
import { Input } from "../../elements/input/Input";
import { Button } from "../../elements/buttons/Button";
import "./AuthPage.css";

export const AuthPage = () => {
    const navigate = useNavigate();
    const { pathname } = useLocation();
    const initial = pathname === "/register" ? "register" : "login";
    const [displayForm, setDisplayForm] = useState(initial);
    const [currentForm, setCurrentForm] = useState(initial);
    const [boxPosition, setBoxPosition] = useState(initial);
    const [hasAnimated, setHasAnimated] = useState(false);
    const [textPosition, setTextPosition] = useState(initial);
    const [contentVisible, setContentVisible] = useState(true);

    const handleSwitch = (to) => {
        setHasAnimated(true);
        setCurrentForm(to);
        setBoxPosition(to);

        setTimeout(() => {
            setDisplayForm(to);
            setTextPosition(to);
            navigate(to === "register" ? "/register" : "/login");
        }, 550);
    };

    const loginLink = <Link onClick={() => handleSwitch("login")}><span>{"<-"}</span> ¿Ya tenés cuenta? ¡Iniciá sesión!</Link>;
    const registerLink = <Link onClick={() => handleSwitch("register")}>¿No tenés cuenta? ¡Registrate! <span>{"->"}</span></Link>;

    return (
        <div className="auth-page">
            <FondoFachero />
            <div className={`auth-page__text auth-page__text--${textPosition} ${hasAnimated ? `auth-page__text-anim--${currentForm}` : ""}`}>
                {displayForm === "login" ? (
                    <>
                        <h1>Hola, de nuevo</h1>
                        <p>Inicia sesión para continuar donde te quedaste y seguir descubriendo el Huergo</p>
                    </>
                ) : (
                    <>
                        <h1>Bienvenido</h1>
                        <p>Desbloqueá todas las funcionalidades de LaMDHA creando una cuenta</p>
                    </>
                )}
            </div>
            
            <div className={`auth-page__box auth-page__box--${boxPosition}`}>
                    {displayForm === "login" ? (
                        <AuthBox
                            key={currentForm}
                            id={hasAnimated ? currentForm : undefined}
                            titulo="Iniciar sesión"
                            subtitulo="Usá tu correo y contraseña"
                            boton={<Button variant="default">Entrar</Button>}
                            link={registerLink}
                        >
                            <Input name="username">Email</Input>
                            <Input name="password">Contraseña</Input>
                        </AuthBox>
                    ) : (
                        <AuthBox
                            key={currentForm}
                            id={hasAnimated ? currentForm : undefined}
                            titulo="Crear cuenta"
                            subtitulo="Usá tu correo y contraseña"
                            boton={<Button variant="default">Registrarse</Button>}
                            link={loginLink}
                        >
                            <Input name="username">Email</Input>
                            <Input name="password">Contraseña</Input>
                            <Input name="password">Confirmar contraseña</Input>
                        </AuthBox>
                    )}
                </div>
            </div>
    );
};