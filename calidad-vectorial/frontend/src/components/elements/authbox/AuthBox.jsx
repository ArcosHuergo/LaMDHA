import { Link } from "react-router-dom";
import "./AuthBox.css";

export const AuthBox = ({ children, titulo="Título del cuadro", subtitulo, onSubmit, boton, linkExtra }) => {
    return (
        <section className='auth-box'>
            <form className='auth-box__content' onSubmit={onSubmit}>
                <h1 className='auth-box__title'>{titulo}</h1>
                <div className='auth-box__content__inputs'>
                    {children}
                </div>
                <div className={`auth-box__content__button uno`}>
                    {boton}
                </div>
            </form>
            {linkExtra && (
                <div className="auth-box__link-extra">
                <span>or</span>
                {linkExtra}
            </div>
            )}
            <Link className='auth-box__footer' to="/">LaMDHA</Link>
        </section>
    );
};