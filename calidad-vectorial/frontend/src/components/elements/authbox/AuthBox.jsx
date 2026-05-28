import "./AuthBox.css";

export const AuthBox = ({ children, titulo="Título del cuadro", subtitulo, onSubmit, boton, linkExtra }) => {
    return (
        <section className='auth-box'>
            <h1 className='auth-box__title'>{titulo}</h1>
            <form className='auth-box__content' onSubmit={onSubmit}>
                <div className='auth-box__content__inputs'>
                    {children}
                </div>
                <div className={`auth-box__content__button uno`}>
                    {boton}
                </div>
            </form>
            {linkExtra && (
                <div className='auth-box__link-extra'>
                    {linkExtra}
                </div>
            )}
            <h1 className='auth-box__footer'>LaMDHA</h1>
        </section>
    );
};