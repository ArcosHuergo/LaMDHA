import Python from '../../../assets/img/logos/python.svg?react';
import Fastapi from '../../../assets/img/logos/fastapi.svg?react';
import Html from '../../../assets/img/logos/html.svg?react';
import Css from '../../../assets/img/logos/css.svg?react';
import Javascript from '../../../assets/img/logos/javascript.svg?react';
import React from '../../../assets/img/logos/react.svg?react';
import Roboflow from '../../../assets/img/logos/roboflow.svg?react';
import Mysql from '../../../assets/img/logos/mysql.svg?react';
import Github from '../../../assets/img/logos/github.svg?react';

import Aurora from '../../elements/aurora/Aurora';
import './SobreNosotros.css';
import { Button } from '../../elements/buttons/Button';
import { Header } from '../../elements/header/Header';
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

            <Header
                fondo={true}
            />

            <main className="sn-content">
                <article className="sn-content__article">
                    <section className="sn-content__article__section">
                        <h3 className="sn-content__article__section__title">¿Qué es LaMDHA?</h3>
                        <p className="sn-content__article__section__text">
                            LaMDHA es un proyecto desarrollado por estudiantes de 6° año de
                            computadoras del Instituto Huergo que utiliza inteligencia artificial
                            para reconocer en qué parte de la escuela fue tomada una foto.
                            <br />A través de una red neuronal entrenada con imágenes de distintos
                            espacios del colegio, el sistema analiza una fotografía y predice en qué
                            aula, laboratorio o sector de la institución fue tomada.
                        </p>
                    </section>
                    <div className="sn-content__article__delimiter" />
                    <section className="sn-content__article__section">
                        <h3 className="sn-content__article__section__title">
                            Tecnologías utilizadas
                        </h3>
                        <div className="sn-content__article__section__logos">
                            <a
                                href="https://www.python.org/"
                                target="_blank"
                                rel="noopener noreferrer"
                                title="Python"
                            >
                                <Python />
                            </a>

                            <a
                                href="https://fastapi.tiangolo.com/"
                                target="_blank"
                                rel="noopener noreferrer"
                                title="FastAPI"
                            >
                                <Fastapi />
                            </a>

                            <a
                                href="https://developer.mozilla.org/en-US/docs/Web/HTML"
                                target="_blank"
                                rel="noopener noreferrer"
                                title="HTML"
                            >
                                <Html />
                            </a>

                            <a
                                href="https://developer.mozilla.org/en-US/docs/Web/CSS"
                                target="_blank"
                                rel="noopener noreferrer"
                                title="CSS"
                            >
                                <Css />
                            </a>

                            <a
                                href="https://developer.mozilla.org/en-US/docs/Web/JavaScript"
                                target="_blank"
                                rel="noopener noreferrer"
                                title="JavaScript"
                            >
                                <Javascript />
                            </a>

                            <a
                                href="https://react.dev/"
                                target="_blank"
                                rel="noopener noreferrer"
                                title="React"
                            >
                                <React />
                            </a>

                            <a
                                href="https://roboflow.com/"
                                target="_blank"
                                rel="noopener noreferrer"
                                title="Roboflow"
                            >
                                <Roboflow />
                            </a>

                            <a
                                href="https://dev.mysql.com/doc/"
                                target="_blank"
                                rel="noopener noreferrer"
                                title="MySQL"
                            >
                                <Mysql />
                            </a>

                            <a
                                href="https://github.com/"
                                target="_blank"
                                rel="noopener noreferrer"
                                title="GitHub"
                            >
                                <Github />
                            </a>
                        </div>
                    </section>

                    <div className="sn-content__article__delimiter" />
                </article>
            </main>
        </>
    );
};
