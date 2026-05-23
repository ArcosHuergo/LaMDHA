import { AuthBox } from "../../elements/authbox/AuthBox";
import { FondoFachero } from "../../elements/prettybackground/FondoFachero";
import { Input } from "../../elements/input/Input";
import "./IniciarSesion.css"

export const IniciarSesion = () => {
    return (
        <main className="body-login">
            <FondoFachero 
                titulo="¡Bienvenido!"
                texto="Si aún no tienes una cuenta registrate para comenzar..."
            />
            <AuthBox
                titulo="Iniciar sesión"
                subtitulo="Usa tu correro y contraseña"
            >
                <Input placeholder="Email"></Input>
                <Input placeholder="Contraseña"></Input>
            </AuthBox>
        </main>
    )
}