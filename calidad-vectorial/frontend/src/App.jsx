import { BrowserRouter as Router, Routes, Route } from "react-router-dom";
import { Layout } from "./layouts/Layout";
import { SobreNosotros } from "./components/pages/aboutus/SobreNosotros"
import { AuthPage } from "./components/pages/auth/AuthPage";
import { Galeria } from "./components/pages/gallery/Galeria";
import { Mapa } from "./components/pages/map/Mapa";

export const App = () => {
    return (
        <Router>
            <Routes>
                <Route path="/" element={<SobreNosotros/>} />
                <Route path="/login" element={<AuthPage/>} />
                <Route path="/register" element={<AuthPage/>} />
                <Route element={<Layout />}>
                    <Route path="/galeria" element={<Galeria />} />
                    <Route path="/mapa" element={<Mapa/>} />
                </Route>
            </Routes>
        </Router>
    )
}