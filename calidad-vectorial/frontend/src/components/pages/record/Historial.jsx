import { useFetch } from '../../utils/fetch/FetchUtils';
import FlechaDesplegar from '../../../assets/img/icons/flechaDesplegar.svg?react';
import './Historial.css';

export const Historial = () => {
    const {
        data: dataHistorial,
        loading: loadingHistorial,
        error: errorHistorial,
    } = useFetch('registro/feedback');

    return (
        <div className="historial">
            <h1 className="historial__title">Mis búsquedas</h1>
            {loadingHistorial ? (
                <p>Cargando</p>
            ) : (
                <div className='historial__cuadro'>
                    <table className="historial__cuadro__tabla">
                        <thead>
                            <tr>
                                <th>Fecha</th>
                                <th>Sector</th>
                                <th>Piso</th>
                                <th>Tipo</th>
                                <th>Referencia</th>
                                <th>Confianza</th>
                                <th>Acertó</th>
                            </tr>
                        </thead>
                        {dataHistorial ? (
                            <tbody>
                                {dataHistorial.map((registro) => (
                                    <>
                                        <tr key={registro.id}>
                                            <td>{registro.fecha_creacion ? registro.fecha_creacion : '-'}</td>
                                            <td>{registro.sector ? registro.sector : '-'}</td>
                                            <td>{registro.piso ? registro.piso : '-'}</td>
                                            <td>{registro.tipo ? registro.tipo : '-'}</td>
                                            <td>{registro.referencia ? registro.referencia : '-'}</td>
                                            <td>{registro.confianza ? registro.confianza + '%' : '-'}</td>
                                            <td>{registro.acerto ? registro.acerto : '-'}</td>
                                        </tr>
                                    </>
                                ))}
                            </tbody>
                        ) : (
                            <p>{errorHistorial}</p>
                        )}
                    </table>
                </div>
            )}
        </div>
    );
};
