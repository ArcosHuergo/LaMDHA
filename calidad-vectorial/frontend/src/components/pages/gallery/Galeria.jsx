import CircularGallery from '../../elements/gallery/CircularGallery'
import { Button } from "../../elements/buttons/Button";

import fotoAula1 from "../../../assets/img/examplephotos/classroom/fotoAula1.jpg";
import fotoAula2 from "../../../assets/img/examplephotos/classroom/fotoAula2.jpg";
import fotoAula3 from "../../../assets/img/examplephotos/classroom/fotoAula3.jpg";

import fotoPasillo1 from "../../../assets/img/examplephotos/hallway/fotoPasillo1.jpg";
import fotoPasillo2 from "../../../assets/img/examplephotos/hallway/fotoPasillo2.jpg";

import fotoLaboratorioInformatica from "../../../assets/img/examplephotos/laboratory/fotoLaboratorioInformatica.jpg";
import fotoLaboratorioQuimica from "../../../assets/img/examplephotos/laboratory/fotoLaboratorioQuimica.jpg";

import fotoBiblioteca from "../../../assets/img/examplephotos/library/fotoBiblioteca.jpg";

import fotoPatioArriba from "../../../assets/img/examplephotos/yard/fotoPatioArriba.jpg";
import fotoPatioKiosco from "../../../assets/img/examplephotos/yard/fotoPatioKiosco.jpg";

import "./Galeria.css"

const items = [
  {
    image: fotoAula1,
    text: 'Aula',
  },
  {
    image: fotoAula2,
    text: 'Aula',
  },
  {
    image: fotoAula3,
    text: 'Aula',
  },
  {
    image: fotoPasillo1,
    text: 'Pasillo',
  },
  {
    image: fotoPasillo2,
    text: 'Pasillo',
  },
  {
    image: fotoLaboratorioInformatica,
    text: 'Laboratorio',
  },
  {
  image: fotoLaboratorioQuimica,
    text: 'Laboratorio',
  },
  {
    image: fotoBiblioteca,
    text: 'Biblioteca',
  },
  {
    image: fotoPatioArriba,
    text: 'Patio',
  },
  {
    image: fotoPatioKiosco,
    text: 'Patio',
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