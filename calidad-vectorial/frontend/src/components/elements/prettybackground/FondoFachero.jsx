import Grainient from "../gradient/Gradient";
import "./FondoFachero.css";

export const FondoFachero = ({children}) => {
    return (
        <aside className="fondo-fachero">
            <div className="fondo-fachero__gradient">
                <Grainient
                    color1="#7F0090"
                    color2="#4F0084"
                    color3="#004AB8"
                    timeSpeed={1.25}
                    colorBalance={0}
                    warpStrength={1}
                    warpFrequency={5}
                    warpSpeed={2}
                    warpAmplitude={50}
                    blendAngle={0}
                    blendSoftness={0.05}
                    rotationAmount={500}
                    noiseScale={2}
                    grainAmount={0.2}
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