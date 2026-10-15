import { useState } from 'react';
import { useFetch } from '../../utils/fetch/FetchUtils';
import FlechaDesplegar from '../../../assets/img/icons/flechaDesplegar.svg?react';
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

    return (
        <div className="historial">
            <h1 className="historial__title">Mis búsquedas</h1>
            {loadingHistorial ? (
                <p>Cargando</p>
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

                    {dataHistorial ? (
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
                                        <button
                                            className="historial__flecha"
                                            onClick={() => handleSelect(registro.id)}
                                        >
                                            <FlechaDesplegar className={`historial__flecha__svg historial__flecha__svg--${seleccionado ? 'seleccionado' : ''}`} />
                                        </button>
                                    </li>
                                )
                            })}
                        </ul>
                    ) : (
                        <p>{errorHistorial}</p>
                    )}
                </div>
            )}
        </div>
    );
};