import { AuthBox } from "../../elements/authbox/AuthBox";
import { FondoFachero } from "../../elements/prettybackground/FondoFachero";
import { Input } from "../../elements/input/Input";
import { Button } from "../../elements/buttons/Button";
import { Link } from "react-router-dom";
import "./IniciarSesion.css"

export const IniciarSesion = () => {
    return (
        <main className="body-login">
            <FondoFachero
                titulo="Hola, de nuevo"
                texto="Inicia sesión para continuar donde te quedaste y seguir descubriendo el Huergo"
            />
            <AuthBox
                titulo="Iniciar sesión"
                subtitulo="Usa tu correro y contraseña"
                boton={<Button variant="default">Entrar</Button>}
                link={<Link to="/register">Aún no tienes cuenta... ¡Creála!</Link>}
            >
                <Input name="username">Email</Input>
                <Input name="password">Contraseña</Input>
            </AuthBox>
        </main>
    )
}