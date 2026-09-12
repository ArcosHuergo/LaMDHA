import { pisos } from "../../data/pisos";

export const PlanoPiso = ({ piso, predicciones }) => {
    const data = pisos[piso];
    if (!data) return null;

    const prediccionesPorZona = new Map(
        predicciones.map((p) => [p.clase, p.confianza])
    );

    const { width, height, image, zonas } = data;

    function getColorForConfidence(confidence) {
        if (confidence === null || confidence === undefined) {
            return "hsl(0, 0%, 60%)";
        }

        const clamped = Math.max(0, Math.min(1, confidence));
        const hue = clamped * 120;
        return `hsl(${hue}, 80%, 50%)`;
}

    return (
        <svg
            viewBox={`0 0 ${width} ${height}`}
            style={{ width: "100%", height: "auto", display: "block" }}
        >
            <image href={image} width={width} height={height} preserveAspectRatio="none" />
            {zonas.map((zona) => {
                const confidence = prediccionesPorZona.get(zona.className);
                const color = getColorForConfidence(confidence);

                return (
                    <polygon
                        key={zona.classId}
                        points={zona.points}
                        fill={color}
                        fillOpacity={0.5}
                        stroke="black"
                        strokeWidth={1}
                    >
                        <title>{zona.className}</title>
                    </polygon>
                );
            })}
        </svg>
    );
}