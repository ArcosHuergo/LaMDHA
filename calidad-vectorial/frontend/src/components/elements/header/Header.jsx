import { useAuth } from '../../utils/auth/AuthContext';
import { useFetch, usePost } from '../../utils/fetch/FetchUtils';
import { useState } from 'react';
import { Link, useLocation, useNavigate } from 'react-router-dom';

import LaMDHA from '../../../assets/img/brand/lamdha.svg?react';
import Usuario from '../../../assets/img/icons/usuario.svg?react';

import { Button } from '../buttons/Button';

import './Header.css';

const ITEMS_NAVEGACION = [
    { to: '/', label: 'Inicio' },
    { to: '/galeria', label: 'Galería' },
    { to: '/mapa', label: 'Mapa' },
    { to: '/historial', label: 'Historial' },
];

export const Header = () => {
    const { usuario, refrescar } = useAuth();
    const navigate = useNavigate();
    const location = useLocation();
    const url = location.pathname;
    const [mostrarLogOut, setMostrarLogOut] = useState(false)
    const { data: dataUsuario, error: errorToken } =
        useFetch('auth/validar-token');
    const { execute: executeLogOut } = usePost('auth/logout');

    const handleLogout = async () => {
        await executeLogOut();
        await refrescar();
        navigate('/');
    };

    return (
        <header className='header'>
            <div className="header__item header__marca">
                <Link to="/" className="header__item__logo">
                    <LaMDHA className="header__item__logo" />
                </Link>

                <Link to="/" className="header__item__marca">
                    LaMDHA
                </Link>
            </div>

            <nav className="header__nav" aria-label="Navegación principal">
                {ITEMS_NAVEGACION.map(({ to, label }) => {
                    if (to === url) {
                        return (
                            <p
                                key={to}
                                className={`header__nav__link header__nav__link--seleccionado header__nav__link--${label}`}
                            >
                                {label}
                            </p>
                        );
                    } else {
                        return (
                            <Link
                                key={to}
                                to={to}
                                className={`header__nav__link header__nav__link--deseleccionado header__nav__link--${label} header__nav__link--${errorToken && label === 'Historial' ? 'ocultar' : ''}`}
                            >
                                {label}
                            </Link>
                        );
                    }
                })}
            </nav>

            {usuario ? (
                <div className="header__item header__item--usr">
                    <p className='header__item__usuario'>{dataUsuario.username}</p>
                    <button className='header__item__logo header__item__logo--usuario'
                        onClick={() => {mostrarLogOut ? setMostrarLogOut(false) : setMostrarLogOut(true)}}
                    >
                        <Usuario />
                        { mostrarLogOut && (
                            <div className='header__item__logo__panel'
                                onClick={handleLogout}
                            >
                                <svg
                                    className='header__item__logo__curva'
                                    viewBox="0 0 42 30"
                                    preserveAspectRatio="none"
                                    fill="none"
                                    aria-hidden="true"
                                >
                                    <path
                                        d="M86 30 C 90 30, 92 33, 91.5 15"
                                        stroke="currentColor"
                                        strokeWidth="1.5"
                                        strokeLinecap="round"
                                        vectorEffect="non-scaling-stroke"
                                    />
                                </svg>
                                Cerrar sesión
                            </div>
                        )}
                    </button>
                </div>
            ) : (
                <div className="header__item header__item--button">
                    <Button to="/login">Iniciar sesión</Button>
                </div>
            )}
        </header>
    );
};
