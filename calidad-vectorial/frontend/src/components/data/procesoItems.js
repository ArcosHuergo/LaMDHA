import Mapa from '../../assets/img/icons/mapa.svg?react';
import Colegio from '../../assets/img/icons/colegio.svg?react';
import Camara from '../../assets/img/icons/camara.svg?react';
import Etiqueta from '../../assets/img/icons/etiqueta.svg?react';
import Pantalla from '../../assets/img/icons/pantalla.svg?react';
import Computadora from '../../assets/img/icons/computadora.svg?react';
import Engranajes from '../../assets/img/icons/engranajes.svg?react';

export const procesoItems = [
    {
        titulo: 'Relevamiento de los planos',
        texto: 'Solicitamos los planos de la escuela y los depuramos, conservando las paredes y escaleras (borrando cotas y distintas marcaciones que pudiesen generar confusión).',
        orientacion: 'izq',
        icono: Mapa
    },
    {
        titulo: 'Identificación de los sectores',
        texto: 'Organizamos los espacios de acuerdo con la distribución y las nomenclaturas establecidas por la institución. Contemplando aulas, patios, laboratorios y pasillos.',
        orientacion: 'der',
        icono: Colegio
    },
    {
        titulo: 'Recolección de imágenes',
        texto: 'Grabamos videos de los distintos sectores del colegio y seleccionamos fotogramas representativos para construir el conjunto de imágenes del proyecto.',
        orientacion: 'izq',
        icono: Camara
    },
    {
        titulo: 'Preparación del conjunto de datos',
        texto: 'Subimos las imagenes a roboflow y las etiquetamos según correspondían, distinguiendo aulas, sectores y pisos.',
        orientacion: 'der',
        icono: Etiqueta
    },
    {
        titulo: 'Diseño y maquetado de la interfaz',
        texto: 'Planificamos la estructura visual del sistema y elaboramos los maquetados previos a la realizacion del frontend, definiendo la navegación del usuario.',
        orientacion: 'izq',
        icono: Pantalla
    },
    {
        titulo: 'Desarrollo del sistema',
        texto: 'Desarrollamos en paralelo el frontend y el backend, junto con la base de datos para administrar la información de los espacios, las imagenes, los usuarios y su actividad.',
        orientacion: 'der',
        icono: Computadora
    },
    {
        titulo: 'Integración y pruebas finales',
        texto: 'Integramos los distintos componentes del proyecto y realizamos pruebas para  comprobar el correcto funcionamiento del sistema y la identificación.',
        orientacion: 'izq',
        icono: Engranajes
    },
]