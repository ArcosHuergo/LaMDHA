import { useAuth } from '../../utils/auth/AuthContext';
import { Link, useLocation, useNavigate } from 'react-router-dom';

import LaMDHA from '../../../assets/img/brand/lamdha.svg?react';
import Usuario from '../../../assets/img/icons/usuario.svg?react';

import BranchedMenu from '../branchedmenu/BranchedMenu';
import { Button } from '../buttons/Button';

import './Header.css';

const ITEMS_NAVEGACION = [
    { to: '/', label: 'Inicio' },
    { to: '/galeria', label: 'Galería' },
    { to: '/mapa', label: 'Mapa' },
    { to: '/historial', label: 'Historial' },
];

export const Header = ({ fondo = false }) => {
    const location = useLocation();
    const url = location.pathname;
    console.log(url);
    const navigate = useNavigate();
    const { usuario } = useAuth();

    return (
        <header className={`header header-fondo--${fondo ? 'true' : ''}`}>
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
                                className={`header__nav__link header__nav__link header__nav__link--${label}`}
                            >
                                {label}
                            </p>
                        );
                    } else {
                        return (
                            <Link
                                key={to}
                                to={to}
                                className={`header__nav__link header__nav__link--seleccionado header__nav__link--${label} header__nav__link--${usuario && label === 'Historial' ? 'ocultar' : ''}`}
                            >
                                {label}
                            </Link>
                        );
                    }
                })}
            </nav>

            {usuario ? (
                <div className="header__item header__item--usr">
                        <p>{usuario.username}</p>
                    <Usuario className="header__item__logo" />
                </div>
            ) : (
                <div className="header__item header__item--button">
                    <Button to="/login">Iniciar sesión</Button>
                </div>
            )}
        </header>
    );
};
