import { BrowserRouter as Router, Routes, Route } from 'react-router-dom';
import { Layout } from './layouts/Layout';
import { SobreNosotros } from './components/pages/aboutus/SobreNosotros';
import { AuthPage } from './components/pages/auth/AuthPage';
import { Galeria } from './components/pages/gallery/Galeria';
import { Mapa } from './components/pages/map/Mapa';
import { ProtectedRoute } from './components/utils/auth/TokenUtils';
import { Historial } from './components/pages/record/Historial';
import { AuthProvider } from './components/utils/auth/AuthContext';

export const App = () => {
        return (
        <AuthProvider>
            <Router>
                <Routes>
                    <Route path="/" element={<SobreNosotros />} />
                    <Route element={<ProtectedRoute />}>
                        <Route path="/login" element={<AuthPage />} />
                        <Route path="/register" element={<AuthPage />} />
                    </Route>
                    <Route element={<Layout />}>
                        <Route path="/galeria" element={<Galeria />} />
                        <Route path="/mapa" element={<Mapa />} />
                        <Route element={<ProtectedRoute />}>
                            <Route path="/historial" element={<Historial/> } />
                        </Route>
                    </Route>
                </Routes>
            </Router>
        </AuthProvider>
    );
};
