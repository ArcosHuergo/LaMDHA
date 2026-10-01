import { Link } from 'react-router-dom';
import './AuthBox.css';

export const AuthBox = ({
    children,
    titulo = 'Título del cuadro',
    subtitulo,
    onSubmit,
    boton,
    link,
    id,
}) => {
    return (
        <section className="auth-box">
            <form className={`auth-box__content auth-box__content--${id}`} onSubmit={onSubmit}>
                <h1 className="auth-box__content__title">{titulo}</h1>
                <div className="auth-box__content__inputs">{children}</div>
                <div className={`auth-box__content__button`}>{boton}</div>
                <div className="auth-box__content__or">or</div>
                <div className="auth-box__content__link">{link}</div>
            </form>

            <Link className="auth-box__footer" to="/">
                LaMDHA
            </Link>
        </section>
    );
};
