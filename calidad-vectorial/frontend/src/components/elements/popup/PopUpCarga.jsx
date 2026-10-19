import { useEffect, useState } from 'react';

import { Bamboos } from './Bamboos';
import { Pasto } from '../pandha/Pasto';
import { PandhaPensando } from '../pandha/PandhaPensando';

import './PopUpCarga.css';

const MENSAJES = [
    'Mirando cada rincón de la foto',
    'Comparando con los espacios del colegio',
    'Calculando probabilidades',
    'Ubicando el aula en el mapa',
];

const INTERVALO_MENSAJE = 2600;

export const PopUpCarga = () => {
    const [indice, setIndice] = useState(0);

    useEffect(() => {
        const id = setInterval(() => {
            setIndice((i) => (i + 1) % MENSAJES.length);
        }, INTERVALO_MENSAJE);
        return () => clearInterval(id);
    }, []);

    return (
        <div className="carga" role="status" aria-live="polite">
            <div className="carga__card">
                <header className="carga__texto">
                    <h2 className="carga__titulo">
                        Procesando tu imagen
                        <span className="carga__puntos" aria-hidden="true">
                            <span>.</span><span>.</span><span>.</span>
                        </span>
                    </h2>
                    {/* key fuerza el remount para re-disparar la animación de entrada */}
                    <p key={indice} className="carga__mensaje">
                        {MENSAJES[indice]}
                    </p>
                    <div className="carga__barra" aria-hidden="true">
                        <span className="carga__barra__bloque" />
                    </div>
                </header>

                <div className="carga__escena" aria-hidden="true">
                    <div className="carga__brillo" />
                    <div className="carga__bamboos">
                        <Bamboos />
                    </div>
                    <div className="carga__pandha">
                        <PandhaPensando width={260} />
                    </div>
                    <div className="carga__suelo">
                        <Pasto alto={44} />
                    </div>
                </div>
            </div>
        </div>
    );
};
