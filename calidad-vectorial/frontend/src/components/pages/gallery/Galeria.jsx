import { useCallback, useState } from 'react';
import { useNavigate } from 'react-router-dom';
import { usePost, useFetch } from '../../utils/fetch/FetchUtils';

import CircularGallery from '../../elements/gallery/CircularGallery';
import { Button } from '../../elements/buttons/Button';
import { PopUpSeleccion } from '../../elements/popup/PopUpSeleccion';
import { PopUpCarga } from '../../elements/popup/PopUpCarga';

import { items } from '../../data/items';

import './Galeria.css';

export const Galeria = () => {
    const navigate = useNavigate();

    const [fotoSeleccionada, setFotoSeleccionada] = useState(null);
    const [archivo, setArchivo] = useState(null);

    const { loading: loadingVision, error: errorVision, execute: executeVision } = usePost('vision/ubicacion');
    const { error: errorToken } = useFetch('auth/validar-token');

    const handleItemClick = useCallback((item) => {
        setFotoSeleccionada(item);
    }, []);

    const cerrarPopUp = () => {
        setFotoSeleccionada(null);
    };

    const enviarImagen = async (archivoImagen, imagenUrl) => {
        const formData = new FormData();
        formData.append('imagen', archivoImagen);

        const resultado = await executeVision(formData);

        if (resultado) {
            navigate('/mapa', {
                state: {
                    ...resultado,
                    imagenUrl: imagenUrl ?? URL.createObjectURL(archivoImagen),
                },
            });
        }
    };

    const handleEnviarImagen = () => {
        if (!archivo) return;
        enviarImagen(archivo);
    };

    const handleSeleccionarFoto = async () => {
        if (!fotoSeleccionada) return;

        const imagenUrl = fotoSeleccionada.image;

        try {
            const respuestaImagen = await fetch(fotoSeleccionada.image);
            const blob = await respuestaImagen.blob();
            const nombreArchivo = fotoSeleccionada.image.split('/').pop();
            const archivoImagen = new File([blob], nombreArchivo, { type: blob.type });
            cerrarPopUp();

            await enviarImagen(archivoImagen, imagenUrl);
        } catch (err) {
            console.error('No se pudo preparar la imagen seleccionada:', err);
        }
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
                    items={items}
                    bend={1.5}
                    captionBackgroundColor="#4F0084"
                    captionBorderRadius={0.15}
                    captionTextColor="#fafafa"
                    captionFontFamily="Orbitron"
                    captionFontSize={80}
                    captionFontWeight="600"
                    highlightColor="#004AB8"
                    onItemClick={handleItemClick}
                />
            </div>
            <span className="galeria__or">or</span>

            {!errorToken ? (
                <Button
                    variant="subir"
                    file={archivo}
                    onFileChange={setArchivo}
                    onClick={handleEnviarImagen}
                >
                    Sube tu imagen
                </Button>
            ) : (
                <Button to="/login" variant="subir">
                    Sube tu imagen
                </Button>
            )}

            {loadingVision && <PopUpCarga />}

            {fotoSeleccionada && (
                <PopUpSeleccion
                    titulo={fotoSeleccionada.text}
                    foto={fotoSeleccionada.image}
                    onClose={cerrarPopUp}
                    onSeleccionar={handleSeleccionarFoto}
                >
                    {fotoSeleccionada.description}
                </PopUpSeleccion>
            )}
        </main>
    );
};
