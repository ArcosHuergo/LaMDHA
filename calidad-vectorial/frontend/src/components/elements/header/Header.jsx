import { useFetch } from '../../utils/fetch/FetchUtils';

import { Link } from 'react-router-dom';
import LaMDHA from '../../../assets/img/brand/lamdha.svg?react';
import Usuario from '../../../assets/img/icons/usuario.svg?react';

import { Button } from '../buttons/Button';

import './Header.css';

export const Header = ({ fondo=false }) => {
    const { data } = useFetch('auth/validar-token');

    return (
        <header className={`header header-fondo--${fondo ? 'true' : ''}`}> 
            <div>
                <Link to="/" className="header__lamdha">
                    <LaMDHA />
                </Link>
                <Link to="/" className="header__lamdha">
                    LaMDHA
                </Link>
            </div>
            {data ? (
                <div>
                    <Usuario />
                    <p>{data.nickname}</p>
                </div>
            ) : (
                <div>
                    <Button to="/login">Iniciar sesión</Button>
                </div>
            )}
        </header>
    );
};
