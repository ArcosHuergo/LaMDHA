
import { useFetch } from '../../utils/fetch/FetchUtils';
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
    console.log(url)
    const navigate = useNavigate();
    const { data: dataUsuario, error: errorToken } =
        useFetch('auth/validar-token');

    return (
        <header className={`header header-fondo--${fondo ? 'true' : ''}`}>
            <div className="header__item header__marca">
                <Link to="/" className="header__item__lamdha">
                    <LaMDHA />
                </Link>

                <Link to="/" className="header__item__lamdha">
                    LaMDHA
                </Link>
            </div>

            <nav className="header__nav" aria-label="Navegación principal">
                {ITEMS_NAVEGACION.map(({ to, label }) => {
                    if (to === url) {
                        return(
                            <p
                                key={to}
                                className='header__nav__link'
                            >
                                {label}
                            </p>
                        )
                    } else {
                        return(
                            <Link
                                key={to}
                                to={to}
                                className='header__nav__link'
                            >
                                {label}
                            </Link>
                        )
                    }
                })}
            </nav>

            {!errorToken ? (
                <div className="header__item header__item--usr">
                        <p>{dataUsuario.username}</p>
                        <Usuario />
                </div>
            ) : (
                <div className="header__item">
                    <Button to="/login">Iniciar sesión</Button>
                </div>
            )}
        </header>
    );
};
