import { Navigate, Outlet, useLocation } from 'react-router-dom';
import { useAuth } from './AuthContext';

export const ProtectedRoute = () => {
    const { usuario, cargando } = useAuth();
    const url = useLocation();

    if (cargando) {
        return (
            <div style={{ textAlign: 'center', marginTop: '2rem' }}>
                Verificando autenticación...
            </div>
        );
    }
    if (usuario) {
        if (url.pathname === '/login' || url.pathname === '/register') {
            return <Navigate to="/" replace />;
        } else {
            return <Outlet />;
        }
    } else {
        if (url.pathname !== '/login' && url.pathname !== '/register') {
            return <Navigate to="/login" replace />;
        } else {
            return <Outlet />;
        }
    }
};