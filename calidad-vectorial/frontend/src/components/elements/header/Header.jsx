import { useFetch } from '../../utils/fetch/FetchUtils';

import { Link, useNavigate } from 'react-router-dom';

import LaMDHA from '../../../assets/img/brand/lamdha.svg?react';
import Usuario from '../../../assets/img/icons/usuario.svg?react';

import BranchedMenu from '../branchedmenu/BranchedMenu';
import { Button } from '../buttons/Button';

import './Header.css';

export const Header = ({ fondo=false }) => {
    const navigate = useNavigate();
    const { dataUsuario } = useFetch('auth/validar-token');

    return (
        <header className={`header header-fondo--${fondo ? 'true' : ''}`}> 
            <div className='header__item'>
                <Link to="/" className="header__item__lamdha">
                    <LaMDHA />
                </Link>
                <Link to="/" className="header__item__lamdha">
                    LaMDHA
                </Link>
            </div>
            {dataUsuario ? (
                <div className='header__item header__item--usr'>
                    <div className='header__item__nav'>
                        <BranchedMenu
                            items={[
                                {
                                    value: 'menu-usuario',
                                    label: <Usuario />,
                                    children: [
                                        { value: '#', label: dataUsuario.username, static: true},
                                        { value: '/historial', label: 'Historial'},
                                    ]
                                }
                            ]}
                            defaultOpen={[1]}
                            defaultActive="#"
                            onSelect={(value) => navigate(value)}
                            color="#fafafa"
                            accentColor="#fafafa"
                            lineColor="#3f3f46"
                            width={240}
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
                </div>
            ) : (
                <div>
                    <Button to="/login">Iniciar sesión</Button>
                </div>
            )}
        </header>
    );
};
