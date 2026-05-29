import { AuthBox } from "../../elements/authbox/AuthBox";
import { FondoFachero } from "../../elements/prettybackground/FondoFachero";
import { Input } from "../../elements/input/Input";
import { Button } from "../../elements/buttons/Button";
import "./IniciarSesion.css"

export const IniciarSesion = () => {
    return (
        <main className="body-login">
            <FondoFachero
                titulo=""
                texto=""
            />
            <AuthBox
                titulo="Iniciar sesión"
                subtitulo="Usa tu correro y contraseña"
                boton={<Button variant="default">Entrar</Button>}
                linkExtra={<Button variant="default" to="/register">Registrarse</Button>}
            >
                <Input name="username">Email</Input>
                <Input name="password">Contraseña</Input>
            </AuthBox>
        </main>
    )
}