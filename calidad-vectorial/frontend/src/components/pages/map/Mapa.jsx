import { useState } from 'react';
import { useLocation } from 'react-router-dom';

import { usePost } from '../../utils/fetch/FetchUtils';

import PulgarArriba from '../../../assets/img/icons/pulgarArriba.svg?react';
import PulgarAbajo from '../../../assets/img/icons/pulgarAbajo.svg?react';

import { PlanoPiso } from '../../elements/floor/PlanoPiso';
import { FachadaPisos } from '../../elements/floor/FachadaPisos';
import { AscensorPisos } from '../../elements/floor/AscensorPisos';

import { Button } from '../../elements/buttons/Button';

import './Mapa.css';

export const Mapa = () => {
    const location = useLocation();
    const resultado = location.state;

    const predicciones = resultado ? resultado.predicciones : undefined;
    const confianza = resultado ? resultado.predicciones[0].confianza * 100 : '';
    const id = resultado ? resultado.registro_id : undefined;

    const a = resultado ? JSON.stringify(resultado) : '';

    const [pisoActual, setPisoActual] = useState('P1');

    const { loading, error, execute } = usePost(`registro/${id}/feedback`, 'PATCH');

    const handle_opinion = async (event) => {
        const resultado = await execute({
            prediccion_correcta: event.currentTarget.value,
        });

        if (resultado) {
            console.log('a');
        }
    };

    return (
        <main className="mapa">
            <div className="mapa__izq">
                <div className="mapa__izq__img">
                    <PlanoPiso piso={pisoActual} predicciones={predicciones} />
                </div>
                <div className="mapa__izq__button">
                    <Button to="/galeria">{'← Volver'}</Button>
                </div>
            </div>
            <div className="mapa__side">
                <article className="mapa__side__cuadro">
                    <div className="mapa__side__cuadro__data">
                        <h2>Aula</h2>
                        <p>Sector</p>
                        <p>Aula teórica</p>
                        {/* <p>{a}</p> */}
                    </div>
                    <div className="mapa__side__cuadro__probabilidad">
                        <p>{confianza}% de probabilidades de que estés en esta aula</p>
                    </div>
                </article>

                <div className="mapa__side__opinion">
                    <p>¿La predicción fue correcta?</p>
                    <div className="mapa__side__opinion__botones">
                        {id != null ? (
                            <button
                                className="mapa__side__opinion__svg"
                                onClick={handle_opinion}
                                value={true}
                            >
                                <PulgarArriba />
                            </button>
                        ) : (
                            <div className="mapa__side__opinion__svg">
                                <PulgarArriba />
                            </div>
                        )}
                        {id != null ? (
                            <button
                                className="mapa__side__opinion__svg"
                                onClick={handle_opinion}
                                value={false}
                            >
                                <PulgarAbajo />
                            </button>
                        ) : (
                            <div className="mapa__side__opinion__svg">
                                <PulgarAbajo />
                            </div>
                        )}
                    </div>
                </div>

                <div className="mapa__side__fachada">
                    <FachadaPisos pisoActual={pisoActual} onClick={setPisoActual} />
                </div>
            </div>
        </main>
    );
};
