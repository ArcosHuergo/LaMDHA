import "./AuthBox.css";
import logo from "../../../assets/img/logo.png"

export const AuthBox = ({ children, titulo="Título del cuadro", onSubmit, botonDer, botonIzq, linkExtra }) => {
    const botones = botonIzq ? 'dos' : 'uno';
    return (
        <section className='auth-box'>
            <div className='auth-box__background'>
                <img src={logo} alt='logo' className='auth-box__background__image'></img>
            </div>
            <h1 className='auth-box__title'>{titulo}</h1>
            <form className='auth-box__content' onSubmit={onSubmit}>
                <div className='auth-box__content__inputs'>
                    {children}
                </div>
                <div className={`auth-box__content__button ${botones}`}>
                    {botonIzq}
                    {botonDer}
                </div>
            </form>
            {linkExtra && (
                <div className='auth-box__link-extra'>
                    {linkExtra}
                </div>
            )}
            <h1 className='auth-box__footer'>Bücher</h1>
        </section>
    );
};