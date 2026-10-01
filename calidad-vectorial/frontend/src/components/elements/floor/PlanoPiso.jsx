import { pisos } from '../../data/pisos';

export const PlanoPiso = ({ piso, predicciones, zonaSeleccionada, onZonaClick }) => {
    const data = pisos[piso];
    if (!data) return null;

    const prediccionesPorZona = predicciones
        ? new Map(predicciones.map((p) => [p.clase, p.confianza]))
        : null;

    const { width, height, image, zonas } = data;

    if (typeof zonaSeleccionada === "string") {
        for (let i = 0; i < zonas.length; i++) {
            if (zonas[i].className === zonaSeleccionada) {
                onZonaClick?.(zonas[i]);
                break;
            }
        }
    }

    function getColorForConfidence(confidence) {
        if (confidence === null || confidence === undefined) {
            return 'hsl(0, 0%, 60%)'; // hsl(0, 85%, 54%)
        }

        const clamped = Math.max(0, Math.min(1, confidence));
        const hue = clamped * 120;
        return `hsl(${hue}, 80%, 50%)`;
    }

    return (
        <svg
            viewBox={`0 0 ${width} ${height}`}
            style={{ width: '100%', height: 'auto', display: 'block' }}
        >
            <image href={image} width={width} height={height} preserveAspectRatio="none" />
            {zonas.map((zona) => {
                const confidence =
                    prediccionesPorZona != null && prediccionesPorZona != undefined
                        ? prediccionesPorZona.get(zona.className)
                        : null;
                const color = getColorForConfidence(confidence);
                const activa = zona.className === zonaSeleccionada?.className;

                return (
                    <polygon
                        key={zona.classname}
                        points={zona.points}
                        fill={color}
                        fillOpacity={activa? 0.6 : 0.5}
                        stroke={activa ? "#FAFAFA" : "#060010"}
                        strokeWidth={activa ? 2.5 : 1}
                        style={{ cursor: "pointer" }}
                        onClick={() => onZonaClick?.(zona)}
                    >
                        <title>{zona.className}</title>
                    </polygon>
                );
            })}
        </svg>
    );
};
