import CircularGallery from '../../elements/gallery/CircularGallery'
import { Button } from "../../elements/buttons/Button";

import imagen from "../../../assets/img/photos/image.jpg"
import "./Galeria.css"

const items = [
  {
    image: '/image.jpg',
    text: 'Foto 1',
  },
  {
    image: '/image.jpg',
    text: 'Foto 2',
  },
  {
    image: '/image.jpg',
    text: 'Foto 3',
  },
  {
    image: '/image.jpg',
    text: 'Foto 4',
  },
];
export const Galeria = () => {
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
                    highlightColor="#7F0090"
                    onItemClick={(item, index) => console.log(item, index)}
                />
            </div>
            <span className='galeria__or'>or</span>
            
            <Button variant='subir'>Sube tu imagen</Button>
        </main>
    );
}