import { useFetch } from '../../utils/fetch/FetchUtils';

export const Historial = () => {
    const { data, loading, error } = useFetch('registro/feedback');

    return (
        <div className="">
            {loading ? (
                <p>Cargando</p>
            ) : (   
                <div className="">        
                    {data ? (
                        <div className="">    
                            {data.map((registro) => (
                                <li>{ registro.fecha }</li> 
                            ))}
                        </div>
                    ) : (
                        <p>{ error }</p>
                    )}
                </div>
            )}
        </div>
    );
};
