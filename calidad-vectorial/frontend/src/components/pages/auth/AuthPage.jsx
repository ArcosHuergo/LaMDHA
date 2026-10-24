import { useState, useRef, useEffect } from 'react';
import { useNavigate, Link, useLocation } from 'react-router-dom';
import { FondoFachero } from '../../elements/prettybackground/FondoFachero';
import { AuthBox } from '../../elements/authbox/AuthBox';
import { Input } from '../../elements/input/Input';
import { Button } from '../../elements/buttons/Button';
import { handleLogin, handleRegister } from '../../utils/auth/AuthUtils';
import { useAuth } from '../../utils/auth/AuthContext';
import { Cargando } from '../../elements/loading/Cargando';
import './AuthPage.css';

export const AuthPage = () => {
    const navigate = useNavigate();
    const { pathname } = useLocation();
    const { refrescar } = useAuth();
    const initial = pathname === '/register' ? 'register' : 'login';
    const [displayForm, setDisplayForm] = useState(initial);
    const [currentForm, setCurrentForm] = useState(initial);
    const [boxPosition, setBoxPosition] = useState(initial);
    const [hasAnimated, setHasAnimated] = useState(false);
    const [textPosition, setTextPosition] = useState(initial);

    const controllerRef = useRef(null);
    const switchTimeoutRef = useRef(null);
    const [username, setUsername] = useState('');
    const [password, setPassword] = useState('');
    const [verificationPassword, setVerificationPassword] = useState('');
    const [error, setError] = useState('');
    const [isDisabled, setIsDisabled] = useState(false);

    useEffect(() => {
        return () => {
            controllerRef.current?.abort();
            clearTimeout(switchTimeoutRef.current);
        };
    }, []);

    const handleSwitch = (to) => {
        clearTimeout(switchTimeoutRef.current);
        setError('');
        setHasAnimated(true);
        setCurrentForm(to);
        setBoxPosition(to);

        switchTimeoutRef.current = setTimeout(() => {
            setDisplayForm(to);
            setTextPosition(to);
            navigate(to === 'register' ? '/register' : '/login');
        }, 550);
    };

    const handleSubmit = (e) => {
        e.preventDefault();
        const params = { username, password, controllerRef, setIsDisabled, setError, refrescar };
        if (currentForm === 'login') {
            handleLogin(params);
        } else {
            handleRegister({ ...params, verificationPassword });
        }
    };

    const loginLink = (
        <Link to="/login" onClick={(e) => { e.preventDefault(); handleSwitch('login'); }}>
            <span>{'<-'}</span> ¿Ya tenés cuenta? ¡Iniciá sesión!
        </Link>
    );
    const registerLink = (
        <Link to="/register" onClick={(e) => { e.preventDefault(); handleSwitch('register'); }}>
            ¿No tenés cuenta? ¡Registrate! <span>{'->'}</span>
        </Link>
    );

    return (
        <div className="auth-page">
            <FondoFachero />
            <div
                className={`auth-page__text auth-page__text--${textPosition} ${hasAnimated ? `auth-page__text-anim--${currentForm}` : ''}`}
            >
                {displayForm === 'login' ? (
                    <>
                        <h1>Hola, de nuevo</h1>
                        <p>
                            Inicia sesión para continuar donde te quedaste y seguir descubriendo el
                            Huergo
                        </p>
                    </>
                ) : (
                    <>
                        <h1>Bienvenido</h1>
                        <p>Desbloqueá todas las funcionalidades de LaMDHA creando una cuenta</p>
                    </>
                )}
            </div>

            <div className={`auth-page__box auth-page__box--${boxPosition}`}>
                {displayForm === 'login' ? (
                    <AuthBox
                        key={currentForm}
                        id={hasAnimated ? currentForm : undefined}
                        titulo="Iniciar sesión"
                        subtitulo="Usá tu correo y contraseña"
                        boton={
                            <Button variant="default" type="submit" isDisabled={isDisabled}>
                                Entrar
                            </Button>
                        }
                        link={registerLink}
                        onSubmit={handleSubmit}
                    >
                        <Input
                            name="username"
                            type="email"
                            autoComplete="username"
                            value={username}
                            onChange={(e) => setUsername(e.target.value)}
                        >
                            Email
                        </Input>
                        <Input
                            name="password"
                            type="password"
                            value={password}
                            autoComplete="current-password"
                            onChange={(e) => setPassword(e.target.value)}
                        >
                            Contraseña
                        </Input>
                        {isDisabled ? ( 
                            <Cargando texto="Cargando login" /> 
                        ) : (
                            error && (
                                <p className="auth-box__error" role="alert">
                                {error}
                                </p>
                            ))
                        }
                    </AuthBox>
                ) : (
                    <AuthBox
                        key={currentForm}
                        id={hasAnimated ? currentForm : undefined}
                        titulo="Crear cuenta"
                        subtitulo="Usá tu correo y contraseña"
                        boton={
                            <Button variant="default" type="submit" isDisabled={isDisabled}>
                                Registrarse
                            </Button>
                        }
                        link={loginLink}
                        onSubmit={handleSubmit}
                    >
                        <Input
                            name="username"
                            type="email"
                            autoComplete="username"
                            value={username}
                            onChange={(e) => setUsername(e.target.value)}
                        >
                            Email
                        </Input>
                        <Input
                            name="password"
                            type="password"
                            value={password}
                            autoComplete="new-password"
                            onChange={(e) => setPassword(e.target.value)}
                        >
                            Contraseña
                        </Input>
                        <Input
                            name="verificationPassword"
                            autoComplete="new-password"
                            type="password"
                            value={verificationPassword}
                            onChange={(e) => setVerificationPassword(e.target.value)}
                        >
                            Confirmar contraseña
                        </Input>
                        {isDisabled ? ( 
                            <Cargando texto="Cargando regsiter" /> 
                        ) : (
                            error && (
                                <p className="auth-box__error" role="alert">
                                    {error}
                                </p>
                        ))
                        }
                    </AuthBox>
                )}
            </div>
        </div>
    );
};