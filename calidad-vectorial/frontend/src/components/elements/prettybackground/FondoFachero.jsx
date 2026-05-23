import Grainient from "../gradient/Gradient";
import "./FondoFachero.css";

export const FondoFachero = ({children, titulo, texto}) => {
    return (
        <aside className="fondo-fachero">
            <div className="fondo-fachero__text">
                <h1>{titulo}</h1>
                <p>{texto}</p>
            </div>
            <div className="fondo-fachero__gradient">
                <Grainient
                    color1="#FF9FFC"
                    color2="#5227FF"
                    color3="#B497CF"
                    timeSpeed={0.25}
                    colorBalance={0}
                    warpStrength={1}
                    warpFrequency={5}
                    warpSpeed={2}
                    warpAmplitude={50}
                    blendAngle={0}
                    blendSoftness={0.05}
                    rotationAmount={500}
                    noiseScale={2}
                    grainAmount={0.1}
                    grainScale={2}
                    grainAnimated={false}
                    contrast={1.5}
                    gamma={1}
                    saturation={1}
                    centerX={0}
                    centerY={0}
                    zoom={0.9}
                />
            </div>
        </aside>
    );
};