import { useCallback, useState } from "react";

import CircularGallery from "../../elements/gallery/CircularGallery";
import { Button } from "../../elements/buttons/Button";
import { PopUpSeleccion } from "../../elements/popup/PopUpSeleccion";
import { PopUpCarga } from "../../elements/popup/PopUpCarga";

import { Items } from "./Items";

import "./Galeria.css"

export const Galeria = () => {
    const [fotoSeleccionada, setFotoSeleccionada] = useState(null);

    const handleItemClick = useCallback((item) => {
        setFotoSeleccionada(item);
    }, []);

    const cerrarPopUp = () => {
        setFotoSeleccionada(null);
    };

    return (
        <main className="galeria">
            <h1>¡Elige tu destino!</h1>
            <div
                style={{
                    width: '960px',
                    height: '330px',
                }}
                >
                <CircularGallery
                    items={Items}
                    bend={1.5}
                    captionBackgroundColor="#4F0084"
                    captionBorderRadius={0.15}
                    captionTextColor="#fafafa"
                    captionFontFamily="Orbitron"
                    captionFontSize={80}
                    captionFontWeight="600"
                    highlightColor="#7F0090"
                    onItemClick={handleItemClick}
                />
            </div>
            <span className='galeria__or'>or</span>
            
            <Button variant='subir'>Sube tu imagen</Button>

            {fotoSeleccionada && (
                <PopUpSeleccion
                    titulo={fotoSeleccionada.text}
                    foto={fotoSeleccionada.image}
                    onClose={cerrarPopUp}
                >
                    {fotoSeleccionada.description}
                </PopUpSeleccion>
            )}
            
        </main>
    );
}