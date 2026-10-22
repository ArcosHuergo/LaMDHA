import { postData } from '../fetch/FetchUtils';

async function loginRequest({ username, password }, signal) {
    try {
        const response = await postData('auth/login', { username, password }, signal);
        return response;
    } catch (error) {
        return { ok: false, message: 'Error de conexión' };
    }
}

export const handleLogin = async ({
    username,
    password,
    controllerRef,
    setIsDisabled,
    setError,
    navigate,
    refrescar,
}) => {
    if (controllerRef.current) {
        controllerRef.current.abort();
        controllerRef.current = null;
    }

    const controller = new AbortController();
    controllerRef.current = controller;

    setError('');
    setIsDisabled(true);

    const respond = await loginRequest({ username, password }, controller.signal);

    if (respond.ok) {
        await refrescar();
        navigate('/galeria');
    } else if (respond.message === 'Error de conexión') {
        setError('Error de conexión');
    } else {
        try {
            const jsonResponse = await respond.json();

            if (jsonResponse.errores) {
                setError(Object.values(jsonResponse.errores).join('. '));
            } else if (jsonResponse.title) {
                setError(jsonResponse.title);
            } else if (Array.isArray(jsonResponse.detail)) {
                setError(jsonResponse.detail.map((e) => (e.msg ?? '').replace(/^Value error,\s*/i, '')).join(' '));
            } else if (jsonResponse.detail) {
                setError(jsonResponse.detail);
            } else {
                setError(JSON.stringify(jsonResponse));
            }
        } catch (err) {
            if (err.name !== 'AbortError') {
                setError('Error: ' + err.message);
            }
        } finally {
            if (controllerRef.current === controller) {
                controllerRef.current = null;
            }
            setIsDisabled(false);
        }
    }
};

export const handleRegister = async ({
    username,
    password,
    verificationPassword,
    controllerRef,
    setIsDisabled,
    setError,
    navigate,
    refrescar,
}) => {
    if (controllerRef.current) {
        controllerRef.current.abort();
        controllerRef.current = null;
    }

    const controller = new AbortController();
    controllerRef.current = controller;

    setError('');
    setIsDisabled(true);

    try {
        const respond = await postData(
            'auth/register',
            { username, password, verification_password: verificationPassword },
            controller.signal,
        );

        if (respond.ok) {
            await loginRequest({ username, password });
            await refrescar();
            navigate('/galeria');
        } else {
            const json = await respond.json();
            const { detail } = json;
            // 422 → lista de errores · 400/401/409 → string
            setError(
                Array.isArray(detail)
                    ? detail.map((e) => (e.msg ?? '').replace(/^Value error,\s*/i, '')).join(' ')
                    : detail ?? 'Ocurrió un error. Probá de nuevo.',
            );
        }
    } catch (error) {
        setError('Error de conexión');
    } finally {
        if (controllerRef.current === controller) {
            controllerRef.current = null;
        }
        setIsDisabled(false);
    }
};