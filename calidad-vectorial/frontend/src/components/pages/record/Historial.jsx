import { useFetch } from '../../utils/fetch/FetchUtils';
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
                <table className="historial__tabla">
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
                        <div className="">
                            {dataHistorial.map((registro) => (
                                <div>
                                    <li>{registro.fecha_creacion}</li>
                                    <li>{registro.sector}</li>
                                    <li>{registro.piso}</li>
                                    <li>{registro.tipo}</li>
                                    <li>{registro.referencia}</li>
                                    <li>{registro.confianza}</li>
                                </div>
                            ))}
                        </div>
                    ) : (
                        <p>{errorHistorial}</p>
                    )}
                </table>
            )}
        </div>
    );
};
