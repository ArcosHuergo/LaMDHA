import { AuthBox } from "../../elements/authbox/AuthBox";
import { FondoFachero } from "../../elements/prettybackground/FondoFachero";
import { Input } from "../../elements/input/Input";
import { Button } from "../../elements/buttons/Button";
import { Link } from "react-router-dom";
import "./Registrar.css";

export const Registrar = () => {
    return (
        <main className="body-register">
            <FondoFachero
                titulo="Bienvenido"
                texto="Desbloqueá todas las funcionalidades de LaMDHA creando una cuenta"
            />
            <AuthBox
                titulo="Crear cuenta"
                subtitulo="Usa tu correro y contraseña"
                boton={<Button variant="default">Registrarse</Button>}
                link={<Link to="/login">¿Ya tienes una cuenta? ¡Inicia sesión!</Link>}
            >
                <Input name="username">Email</Input>
                <Input name="password">Contraseña</Input>
                <Input name="password">Confirmar contraseña</Input>
            </AuthBox>
        </main>
    )
}