import { BrowserRouter as Router, Routes, Route } from "react-router-dom";
import { SobreNosotros } from "./components/pages/aboutus/SobreNosotros"

export const App = () => {
    return (
        <Router>
            <Routes>
                <Route path="/" element={<SobreNosotros/>} />
            </Routes>
        </Router>
    )
}