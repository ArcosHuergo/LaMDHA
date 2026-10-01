import { useFetch } from '../../utils/fetch/FetchUtils';

import { Link } from 'react-router-dom';
import LaMDHA from '../../../assets/img/brand/lamdha.svg?react';
import Usuario from '../../../assets/img/icons/usuario.svg?react';

import { Button } from '../buttons/Button';

import './Header.css';

export const Header = () => {
    const { data } = useFetch('auth/me');

    return (
        <header className="header">
            <div>
                <Link to="/" className="header__lamdha">
                    <LaMDHA />
                </Link>
                <Link to="/" className="header__lamdha">
                    LaMDHA
                </Link>
            </div>
            {data != '' && data !== null && data !== undefined ? (
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
