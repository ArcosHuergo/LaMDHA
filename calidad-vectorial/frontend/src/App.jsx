import { BrowserRouter as Router, Routes, Route } from "react-router-dom";
import { SobreNosotros } from "./components/pages/aboutus/SobreNosotros"
import { IniciarSesion } from "./components/pages/login/IniciarSesion";
import { Registrar } from "./components/pages/register/Registrar";

export const App = () => {
    return (
        <Router>
            <Routes>
                <Route path="/" element={<SobreNosotros/>} />
                <Route path="/login" element={<IniciarSesion/>} />
                <Route path="/register" element={<Registrar/>} />
            </Routes>
        </Router>
    )
}