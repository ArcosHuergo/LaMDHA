import { createContext, useCallback, useContext, useEffect, useState } from 'react';
import { getData } from '../fetch/FetchUtils';

const AuthContext = createContext(null);

export const AuthProvider = ({ children }) => {
    const [usuario, setUsuario] = useState(null);
    const [cargando, setCargando] = useState(true);

    const refrescar = useCallback(async (signal) => {
        try {
            const respond = await getData('auth/validar-token', signal);
            setUsuario(respond.ok ? await respond.json() : null);
        } catch (err) {
            if (err.name === 'AbortError') return;
            setUsuario(null);
        }
        setCargando(false);
    }, []);

    useEffect(() => {
        const controller = new AbortController();
        refrescar(controller.signal);
        return () => controller.abort();
    }, [refrescar]);

    return (
        <AuthContext.Provider value={{ usuario, cargando, refrescar }}>
            {children}
        </AuthContext.Provider>
    );
};

export const useAuth = () => useContext(AuthContext);