import { BrowserRouter as Router, Routes, Route } from "react-router-dom";
import { SobreNosotros } from "./components/pages/aboutus/SobreNosotros"
import { AuthPage } from "./components/pages/auth/AuthPage";
import { Index } from "./components/pages/index/Index";

export const App = () => {
    return (
        <Router>
            <Routes>
                <Route path="/" element={<SobreNosotros/>} />
                <Route path="/login" element={<AuthPage/>} />
                <Route path="/register" element={<AuthPage/>} />
                <Route path="/index" element={<Index/>} />
            </Routes>
        </Router>
    )
}