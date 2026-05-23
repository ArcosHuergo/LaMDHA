import Aurora from "../../elements/aurora/Aurora";
//import Button from "../../elements/button/Button";
import "./SobreNosotros.css";
export const SobreNosotros = () => {
    return (
        <>
            <section className="sn-hero">
                <div className="prueba">
					<Aurora
                        colorStops={["#006AB8","#006AB8","#540090"]}
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
                </div>
            </section>

            <header className="header">
                <h2>LaMDHA</h2>
                <p>Ins. Ind. Luis A. Huergo</p>
            </header>

            <section className="sn-content">
                <article className="sn-content__article">
                    <h3 className="sn-content__article__title">¿Qué es LaMDHA?</h3>
                    <p className="sn-content__article__text">
                        LaMDHA es un proyecto desarrollado por estudiantes de 6° año de computadoras  del Instituto Huergo que utiliza inteligencia artificial para reconocer en qué parte de la escuela fue tomada una foto.
                        <br />A través de una red neuronal entrenada con imágenes de distintos espacios del colegio, el sistema analiza una fotografía y predice en qué aula, laboratorio o sector de la institución fue tomada.
                    </p>
                </article>
            </section>
        </>
    )
}