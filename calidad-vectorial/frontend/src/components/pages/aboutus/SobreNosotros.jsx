import Aurora from '../../elements/aurora/Aurora';
import './SobreNosotros.css';

import { Button } from '../../elements/buttons/Button';
import { Header } from '../../elements/header/Header';
import { AboutUsCard } from '../../elements/aboutus/AboutUsCard';
import { DeveloperCard } from '../../elements/aboutus/DeveloperCard';

import { logos } from '../../data/logos';
import { procesoItems } from '../../data/procesoItems';
import { developers } from '../../data/developers';

export const SobreNosotros = () => {
    return (
        <>
            <section className="sn-hero">
                <div className="fondo-aurora">
                    <Aurora
                        colorStops={['#7F0090', '#004AB8', '#4F0084']}
                        blend={1.0}
                        amplitude={1.0}
                        speed={1}
                    />
                </div>
                <div className="sn-hero__text">
                    <h1 className="sn-hero__text__title">LaMDHA</h1>
                    <p className="sn-hero__text__subtitle">
                        Language Model for Detecting Huergo Areas
                    </p>
                    <Button to="/galeria">Descubrir</Button>
                </div>
            </section>

            <main className="sn-content">
                <article className="sn-content__article">
                    <h2 className="sn-content__article__title">¿Qué es LaMDHA?</h2>
                    <p className="sn-content__article__text">
                        LaMDHA es un proyecto desarrollado por estudiantes de 6° año de
                        computadoras del Instituto Huergo que utiliza inteligencia artificial
                        para reconocer en qué parte de la escuela fue tomada una foto.
                        <br />A través de una red neuronal entrenada con imágenes de distintos
                        espacios del colegio, el sistema analiza una fotografía y predice en qué
                        aula, laboratorio o sector de la institución fue tomada.
                    </p>
                </article>
                <div className="sn-content__delimiter" />
                <section className="sn-content__section--logos">
                    <h2 className="sn-content__article__title">
                        Tecnologías utilizadas
                    </h2>
                    <div className="sn-content__section__logos">
                        {logos.map(({ nombre, url, icono: Icono }) => (
                            <a key={nombre} href={url} target="_blank" rel="noopener noreferrer" title={nombre}>
                                <Icono />
                            </a>
                        ))}
                    </div>
                </section>

                <div className="sn-content__delimiter" />

                <section className='sn-content__section'>
                    <h2 className='sn-content__article__title'>Cómo desarrollamos LaMDHA</h2>
                    <div className='sn-content__section__data'>
                        {procesoItems.map((item) => (
                            <AboutUsCard
                                key={item.titulo}
                                titulo={item.titulo}
                                texto={item.texto}
                                orientacion={item.orientacion}
                                icono={item.icono}
                            />
                        ))}
                    </div>
                </section>

                <div className="sn-content__delimiter" />

                <section className='sn-content__section'>
                    <h2 className='sn-content__article__title'>Integrantes del proyecto</h2>
                    <div className='sn-content__section__developers'>
                        {developers.map((developer, index) => (
                            <DeveloperCard
                                key={developer.nombre}
                                nombre={developer.nombre}
                                github={developer.github}
                                correo={developer.correo}
                                avatar={developer.avatar}
                                index={index}
                            />
                        ))}
                    </div>
                </section>

                <div className="sn-content__delimiter" />

            </main>
        </>
    );
};
