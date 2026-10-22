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

export const Header = () => {
    const location = useLocation();
    const url = location.pathname;
    const { data: dataUsuario, error: errorToken } =
        useFetch('auth/validar-token');
    const { execute: executeLogOut } = usePost('auth/logout');

    const handleLogout = async () => {
        await executeLogOut();
        navigate('/');
    };
    const navigate = useNavigate();
    const { usuario } = useAuth();

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
                        <BranchedMenu
                            items={[
                                {
                                    value: 'menu-usuario',
                                    label: <Usuario />,
                                    children: [
                                        { value: '#', label: 'Cerrar sesión'},
                                    ]
                                }
                            ]}
                            className='header__item__logo--usr'
                            defaultOpen={[1]}
                            defaultActive="#"
                            onSelect={handleLogout}
                            color="#fafafa"
                            accentColor="#fafafa"
                            lineColor="#fafafa88"
                            width={45}
                            rowHeight={36}
                            indent={40}
                            trunk={14}
                            radius={10}
                            lineWidth={1.5}
                            fontSize={14}
                            drawDuration={400}
                            foldDuration={300}
                        />
                </div>
            ) : (
                <div className="header__item header__item--button">
                    <Button to="/login">Iniciar sesión</Button>
                </div>
            )}
        </header>
    );
};
