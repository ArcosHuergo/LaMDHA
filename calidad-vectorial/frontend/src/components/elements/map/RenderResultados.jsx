import './RenderResultados.css';

function getColorForConfidence(confidence) {
        if (confidence === null || confidence === undefined) {
            return 'hsl(0, 0%, 60%)';
        }

        const clamped = Math.max(0, Math.min(1, confidence));
        const hue = clamped * 120;
        return `hsl(${hue}, 80%, 50%)`;
    }

export const RenderResultados = ({ predicciones }) => {
    return (
        <ol className="resultados">
            {predicciones?.map((item, index) => {
                const confianza = item.confianza;
                const confianzaClamped = confianza == null
                    ? 0
                    : Math.max(0, Math.min(1, confianza));
                const porcentaje = confianza == null
                    ? '—'
                    : `${Math.round(confianzaClamped * 100)}%`;
                console.log(getColorForConfidence(confianza))

                return (
                    <li
                        key={`${item.clase}`}
                        className="resultados__item"
                    >
                        <div className="resultados__item__encabezado">
                            <span className="resultados__item__indice">{index + 1}</span>
                            <h3 className="resultados__item__clase">{item.clase}</h3>
                        </div>

                        <div className="resultados__item__detalle">
                            <div
                                className="resultados__item__barra"
                                role="progressbar"
                                aria-label={`Confianza de ${item.clase}`}
                                aria-valuemin={0}
                                aria-valuemax={100}
                                aria-valuenow={Math.round(confianzaClamped * 100)}
                            >
                                <div
                                    className="resultados__item__barra__relleno"
                                    style={{
                                        maxWidth: `${confianzaClamped * 100}%`,
                                        backgroundColor: getColorForConfidence(confianza),
                                        animationDuration: `${500 / confianzaClamped}ms`,
                                    }}
                                />
                            </div>
                            <span className="resultados__item__confianza">{porcentaje}</span>
                        </div>
                    </li>
                );
            })}
        </ol>
    );
};