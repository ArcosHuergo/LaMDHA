import { useLocation } from "react-router-dom";

export const Mapa = () => {
    const location = useLocation();
    const resultado = location.state;

    return (
        <main className="mapa">
            <h1>Resultado</h1>
            <pre>{JSON.stringify(resultado, null, 2)}</pre>
        </main>
    );
}