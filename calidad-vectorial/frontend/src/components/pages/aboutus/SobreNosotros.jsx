import Particles from "../../elements/particles/Particles";
import Beams from "../../elements/beams/Beams";
import Aurora from "../../elements/aurora/Aurora";
import "./SobreNosotros.css";
export const SobreNosotros = () => {
    return (
        <>
            <section className="sn-hero">
            	<div className="prueba">
					<Aurora
  					colorStops={["#006AB8","#006AB8","#540090"]}
  					blend={0.5}
  					amplitude={1.0}
  					speed={1}
					/>
	
				</div>
                <div className="sn-hero__text">
                    <h1 className="sn-hero__text__title">LaMDHA</h1>
                    <p className="sn-hero__text__subtitle">
                        Soy una Inteligencia Artifical...
                        <br />Sube una foto dentro del colegio
                        <br />e intentaré ubicarte
                    </p>
                </div>
            </section>

            <header className="header">
                <h2>GeoHuergo</h2>
                <p>Ins. Ind. Luis A. Huergo</p>
            </header>

            <section className="sn-content">
                <article className="sn-content__article">
                    <h3 className="sn-content__article__title">¿Qué es GeoHuergo?</h3>
                    <p className="sn-content__article__text">
                        GeoHuergo es un proyecto desarrollado por estudiantes de 6° año de computadoras  del Instituto Huergo que utiliza inteligencia artificial para reconocer en qué parte de la escuela fue tomada una foto.
                        <br />A través de una red neuronal entrenada con imágenes de distintos espacios del colegio, el sistema analiza una fotografía y predice en qué aula, laboratorio o sector del Huergo fue tomada.
                    </p>
                </article>
            </section>
        </>
    )
}
