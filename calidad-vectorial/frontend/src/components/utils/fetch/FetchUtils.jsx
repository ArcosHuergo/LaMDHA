import { useState, useEffect, useRef, useCallback } from "react";

/** Hook para realizar peticiones GET
*   @param {string} url - endpoint al que se envía el GET
*   @returns { data, loading, error }
*        data: datos de respuesta (JSON o texto)
*        loading: booleano para mostrar spinner
*        error: mensaje de error (string)
**/
export const useFetch = (url) => {
    const [data, setData] = useState([]);
    const [loading, setLoading] = useState(false);
    const [error, setError] = useState("");

    const fetchDataRef = useRef(null);

    useEffect(() => {
        // Controller para poder cancelar la request si el componente se desmonta
        const controller = new AbortController();
        const signal = controller.signal;

        // Función que realiza el GET
        const fetchData = async () => {
            setLoading(true); // arranca el spinner

            try {
                // Realiza la request (pasa la señal para poder abortar)
                const respond = await getData(url, signal);

                if (respond.ok) {
                    // Parseo según content-type de la respuesta
                    const contentType = respond.headers.get("content-type");
                    if (contentType && contentType.includes("application/json")) {
                        const json = await respond.json();
                        setData(json); // setea JSON
                    } else {
                        const text = await respond.text();
                        setData(text); // setea texto plano
                    }
                } else {
                    // Muestra el mensaje de error de spring
                    setError("Error en la respuesta del servidor: " + respond.status + " " + respond.statusText);
                    setLibroMensaje("Error en la respuesta del servidor: " + respond.status + " " + respond.statusText);

                }
            } catch (err) {
                // Ignora AbortError
                if (err.name !== "AbortError") {
                    setError("Error: " + err.message);
                    setLibroMensaje("Error: " + err.message);
                }
            } finally {
                // Cierra el spinner (siempre)
                setLoading(false);
            }
        };
        fetchDataRef.current = fetchData;
        // Dispara el fetch al montar/cambiar la URL
        fetchData();

        // Cleanup: si el componente se desmonta, aborta la request
        return () => controller.abort();
    }, [url]);
        
    const refetch = () => {
        if (fetchDataRef.current) {
            const controller = new AbortController();
            fetchDataRef.current(controller.signal);
        }
    };

    return { data, loading, error, refetch };
};

/** Hook para realizar peticiones POST
*   @param {string} url - endpoint al que se envía el POST
*   @returns { data, loading, error, execute }
*       data: datos de respuesta (JSON o texto)
*       loading: booleano para mostrar spinner
*       error: mensaje de error (string)
*       execute: función para ejecutar el POST
**/
export function usePost(url, method = "POST") {
    // Estado: datos de respuesta, “cargando” y error
    const [data, setData] = useState("");
    const [loading, setLoading] = useState(false);
    const [error, setError] = useState("");

    // Guarda el AbortController de la request activa
    const controllerRef = useRef(null);

    // Flag: evita setState si el componente ya no está montado
    const isMountedRef = useRef(true);

    // Define montaje/desmontaje del componente
    useEffect(() => {
        isMountedRef.current = true;
        return () => {
            isMountedRef.current = false;
            if (controllerRef.current) controllerRef.current.abort();
        };
    }, []);

    // Función que ejecuta el POST (No cambiar nombre ni firma)
    const execute = useCallback(async (payload) => {
        // Si había una request en curso, la cancela antes de iniciar otra
        if (controllerRef.current) {
            controllerRef.current.abort();
            controllerRef.current = null;
        }

        // Crea un nuevo AbortController para esta request
        const controller = new AbortController();
        controllerRef.current = controller;

        // Resetea estados de UI
        if (isMountedRef.current) {
            setLoading(true);
            setError("");
            setLibroMensaje("");
        }

        try {
            // Envía el POST (incluye la señal para poder abortar)
            const respond = await postData(url, payload, controller.signal, method);

            // Si se aborta la request o el componente se desmontó cancela la request
            if (controller.signal.aborted || !isMountedRef.current) return;

            if (respond.ok) {
                // Parseo según content-type de la respuesta
                const contentType = respond.headers.get("content-type");
                if (contentType && contentType.includes("application/json")) {
                    const json = await respond.json();
                    if (isMountedRef.current) setData(json);
                } else {
                    const text = await respond.text();
                    if (isMountedRef.current) setData(text);
                }
            } else {
                // Muestra el mensaje de error de spring
                if (isMountedRef.current) {
                    setError("Error en la respuesta del servidor: " + respond.status + " " + respond.statusText );
                    setLibroMensaje("Error en la respuesta del servidor: " + respond.status + " " + respond.statusText );
                }
            }
        } catch (err) {
            // Ignora AbortError
            if (err.name !== "AbortError" && isMountedRef.current) {
                setError("Error: " + err.message);
                setLibroMensaje("Error: " + err.message);
            }
        } finally {
            // Apaga el spinner y limpia el controller de esta request
            if (isMountedRef.current) setLoading(false);
            controllerRef.current = null;
        }
    }, [url]);

    // Devuelve toda la información y la función para disparar el POST en el handler
    return { data, loading, error, execute };
}

export const postData = async (url, data, signal, method = "POST") => {
    const respond = await fetch("http://localhost:8000/" + url, {
        method: method,
        headers: { "Content-Type": "application/json" },
        body: JSON.stringify(data),
        credentials: "include",
        signal: signal
    });
    return respond;
}

export const getData = async (url, signal) => {
    const respond = await fetch("http://localhost:8000/" + url, {
        method: "GET",
        credentials: "include",
        signal: signal
    });
    return respond;
}