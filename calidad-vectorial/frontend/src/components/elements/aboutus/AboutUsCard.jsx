import './AboutUsCard.css';

export const AboutUsCard = ({ titulo, texto, orientacion, icono: Icono }) => {
    return (
        <article className={`about-us-card about-us-card--${orientacion}`}>
            <h3 className={`about-us-card__title about-us-card__title--${orientacion}`}>{titulo}</h3>
            <p className={`about-us-card__text about-us-card__text--${orientacion}`}>{texto}</p>
            <span className={`about-us-card__circle about-us-card__circle--${orientacion}`}>
                <Icono className='about-us-card__circle__icono' aria-hidden="true" />
            </span>
        </article>
    )
}