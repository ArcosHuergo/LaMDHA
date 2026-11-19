import { useState, useEffect } from "react";
import { useLocation } from "react-router-dom";

import { usePost } from '../../utils/fetch/FetchUtils';
import { useAuth } from '../../utils/auth/AuthContext';

import PulgarArriba from '../../../assets/img/icons/pulgarArriba.svg?react';
import PulgarAbajo from '../../../assets/img/icons/pulgarAbajo.svg?react';

import { PlanoPiso } from "../../elements/floor/PlanoPiso";
import { FachadaPisos } from "../../elements/floor/FachadaPisos";
import { CuadroZona } from "../../elements/map/CuadroZona";
import { Pestanas } from "../../elements/tab/Pestanas";

import { Button } from '../../elements/buttons/Button';

import './Mapa.css';

const COLORES_CONFETI = ['#ff4d6d', '#ffd23f', '#3bceac', '#4cc9f0', '#b388ff', '#ff9f1c'];

const crearParticulas = (cantidad = 18) =>
    Array.from({ length: cantidad }, (_, i) => ({
        id: i,
        dx: (Math.random() - 0.5) * 140,
        dy: -(30 + Math.random() * 70),
        rot: Math.random() * 720,
        delay: Math.random() * 80,
        color: COLORES_CONFETI[i % COLORES_CONFETI.length],
    }));

const PISOS = [
    { id: 'PB', nombre: 'Planta Baja' },
    { id: 'EPB', nombre: 'Entrepiso PB' },
    { id: 'P1', nombre: 'Primer Piso' },
    { id: 'EP1', nombre: 'Entrepiso P1' },
    { id: 'P2', nombre: 'Segundo Piso' },
    { id: 'P3', nombre: 'Tercer Piso' },
];

export const Mapa = () => {
    const location = useLocation();
    const resultado = location.state;

    const imagenUrl = resultado ? resultado.imagenUrl : undefined;

    const predicciones = resultado ? resultado.predicciones : undefined;
    const id = resultado ? resultado.registro_id : undefined;
    const piso = resultado ? resultado.piso : 'PB';
    const zona = resultado ? resultado.predicciones[0].clase : undefined

    const [pisoActual, setPisoActual] = useState(piso);
    const [zonaSeleccionada, setZonaSeleccionada] = useState(zona);
    const [tab, setTab] = useState('Resultados');

    const confianzaSeleccionada = zonaSeleccionada
        ? predicciones?.find((p) => p.clase === zonaSeleccionada.className)?.confianza ?? null : null;

    const { execute: executeFeedback } = usePost(`registro/feedback/${id}`, "PATCH");

    const { usuario } = useAuth();

    const [enviando, setEnviando] = useState(false);
    const [voto, setVoto] = useState(null);
    const [confeti, setConfeti] = useState(null);

    const handle_opinion = async (event) => {
        if (enviando) return;

        const valor = event.currentTarget.value;

        setEnviando(true);
        setVoto(valor);

        const key = Date.now();
        setConfeti({ key, tipo: valor, particulas: crearParticulas() });
        setTimeout(() => setConfeti((c) => (c?.key === key ? null : c)), 1100);

        try {
            await executeFeedback({ prediccion_correcta: valor });
            await new Promise((resolve) => setTimeout(resolve, 2000));
        } finally {
            setEnviando(false);
        }
    };

    return (
        <main className="mapa">
            <header className="mapa__header">
                <Button to='/galeria'>{'← volver'}</Button>

                {zona && (
                    <div className="mapa__header__info">
                        <h1>Estás en {zona}</h1>

                        {id && (
                            <div className="mapa__opinion" role="group" aria-label="¿La predicción fue correcta?">
                                <span className="mapa__opinion__texto">¿Acertamos?</span>

                                {[
                                    { valor: 'true', Icono: PulgarArriba, label: 'La predicción fue correcta' },
                                    { valor: 'false', Icono: PulgarAbajo, label: 'La predicción fue incorrecta' },
                                ].map(({ valor, Icono, label }) => (
                                    <div className="mapa__opinion__celda" key={valor}>
                                        <button
                                            type="button"
                                            className={`mapa__opinion__btn ${voto === valor ? 'mapa__opinion__btn--activo' : ''}`}
                                            onClick={handle_opinion}
                                            value={valor}
                                            disabled={enviando}
                                            aria-label={label}
                                            title={label}
                                        >
                                            <Icono />
                                        </button>

                                        {confeti?.tipo === valor && (
                                            <span className="confeti" key={confeti.key} aria-hidden="true">
                                                {confeti.particulas.map((p) => (
                                                    <i
                                                        key={p.id}
                                                        style={{
                                                            '--dx': `${p.dx}px`,
                                                            '--dy': `${p.dy}px`,
                                                            '--rot': `${p.rot}deg`,
                                                            '--delay': `${p.delay}ms`,
                                                            background: p.color,
                                                        }}
                                                    />
                                                ))}
                                            </span>
                                        )}
                                    </div>
                                ))}
                            </div>
                        )}
                    </div>
                )}
            </header>
            <section className="mapa__plano contenedor">
                <header className="mapa__plano__header">
                    <h2 className="mapa__plano__titulo">
                        {PISOS.find((p) => p.id === pisoActual)?.nombre}
                    </h2>
                    <Pestanas
                        items={PISOS}
                        activa={pisoActual}
                        onChange={setPisoActual}
                    />
                </header>

                <div className="mapa__plano__img">
                    <PlanoPiso
                        piso={pisoActual}
                        predicciones={predicciones}
                        zonaSeleccionada={zonaSeleccionada}
                        onZonaClick={setZonaSeleccionada}
                        setTab={setTab}
                    />
                </div>

                <footer className="mapa__plano__leyenda">
                    <span>Menos probable</span>
                    <div className="mapa__plano__barra" />
                    <span>Más probable</span>
                </footer>
            </section>

            <section className="mapa__side">
                <div className="mapa__side__img contenedor">
                    {imagenUrl ? (<>
                        <img src={imagenUrl} alt="Imagen ingresada" />
                        <span>TU FOTO</span>
                    </>) : (
                        <div className='mapa__side__img__galeria'>
                            <p>Carga una imagen en galería para obtener una predicción</p>
                            <Button to='/galeria'>Galería</Button>
                        </div>
                    )}
                </div>
                <CuadroZona
                    predicciones={predicciones}
                    clase={zonaSeleccionada?.className}
                    tipo={zonaSeleccionada?.tipo}
                    confianza={confianzaSeleccionada}
                    tab={tab}
                    setTab={setTab}
                    logueado={Boolean(usuario)}
                />
            </section>

            {/* <div className="mapa__fachada">
                <FachadaPisos pisoActual={pisoActual} onClick={setPisoActual}/>
            </div> */}

            {/* <div className="mapa__opinion">
                <div className="mapa__side__opinion">
                    <p>¿La predicción fue correcta?</p>
                    <div className="mapa__opinion__botones">
                        {id ? (
                            <button className="mapa__opinion__svg"
                                onClick={handle_opinion}
                                value={true}
                                style={{ cursor: activarOpinion }}
                            >
                                <PulgarArriba />
                            </button>
                        ) : (
                            <div className="mapa__opinion__svg">
                                <PulgarArriba />
                            </div>
                        )}
                        {id ? (
                            <button className="mapa__opinion__svg"
                                onClick={handle_opinion}
                                value={false}
                                style={{ cursor: activarOpinion }}
                            >
                                <PulgarAbajo />
                            </button>
                        ) : (
                            <div className="mapa__opinion__svg">
                                <PulgarAbajo />
                            </div>
                        )}
                    </div>
                </div>
            </div> */}
        </main>
    );
};
