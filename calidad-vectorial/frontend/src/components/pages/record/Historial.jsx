import { useState } from 'react';
import { useFetch } from '../../utils/fetch/FetchUtils';
import { Cargando } from '../../elements/loading/Cargando';
import './Historial.css';

const COLUMNAS = ['Fecha', 'Sector', 'Piso', 'Tipo', 'Referencia', 'Confianza', 'Acertó'];

export const Historial = () => {

    const [registroSeleccionado, setRegistro] = useState();

    const {
        data: dataHistorial,
        loading: loadingHistorial,
        error: errorHistorial,
    } = useFetch('registro/feedback');

    const handleSelect = (id) => {
        setRegistro((actual) => (actual === id ? null : id));
    }

    console.log(dataHistorial);

    return (
        <div className="historial">
            <h1 className="historial__title">Mis búsquedas</h1>
            {loadingHistorial ? (
                <Cargando texto='Cargando' />
            ) : (
                <div className="historial__cuadro">
                    <div className="historial__cabecera">
                        {COLUMNAS.map((columna) => (
                            <span key={columna} className="historial__celda">
                                {columna}
                            </span>
                        ))}
                        <span className="historial__flecha" aria-hidden="true" />
                    </div>

                    {dataHistorial && dataHistorial.length !== 0 ? (
                        <ul className="historial__lista">
                            {dataHistorial.map((registro) => {
                                const seleccionado = registroSeleccionado === registro.id;

                                return (
                                    <li key={registro.id} className="historial__fila">
                                        <span className="historial__celda">{registro.fecha_creacion || '-'}</span>
                                        <span className="historial__celda">{registro.sector || '-'}</span>
                                        <span className="historial__celda">{registro.piso || '-'}</span>
                                        <span className="historial__celda">{registro.tipo || '-'}</span>
                                        <span className="historial__celda">{registro.referencia || '-'}</span>
                                        <span className="historial__celda">
                                            {registro.confianza ? registro.confianza + '%' : '-'}
                                        </span>
                                        <span className="historial__celda">
                                            {registro.prediccion_correcta !== null
                                                ? registro.prediccion_correcta ? 'Sí' : 'No'
                                                : '-'}
                                        </span>
                                    </li>
                                )
                            })}
                        </ul>
                    ) : !errorHistorial ? (
                        <div className='historial__cargando'>
                            <Cargando texto='Cargando historial' />
                        </div>
                    ) : (
                        <p>{errorHistorial}</p>
                    )}
                </div>
            )}
        </div>
    );
};