import './DeveloperCard.css';

export const DeveloperCard = ({ nombre, github, correo, avatar, index }) => {
    return (
        <article className={`developer-card developer-card--${index}`}>
            <div className='developer-card__data'>
                <h3 className='developer-card__data__nombre'>{nombre}</h3>
                <p className='developer-card__data__texto'>Usuario de GitHub: {github}</p>
                <p className='developer-card__data__texto'>Correo: {correo}</p>
            </div>
            <img className='developer-card__img' src={avatar} alt="" />
        </article>
    )
}