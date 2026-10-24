import { postData } from '../fetch/FetchUtils';

async function loginRequest({ username, password }, signal) {
    try {
        const response = await postData('auth/login', { username, password }, signal);
        return response;
    } catch (error) {
        if (error.name === 'AbortError') {
            return { ok: false, message: 'AbortError' };
        }
        return { ok: false, message: 'Error de conexión' };
    }
}

export const handleLogin = async ({
    username,
    password,
    controllerRef,
    setIsDisabled,
    setError,
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
        const respond = await loginRequest({ username, password }, controller.signal);

        if (respond.ok) {
            await refrescar();
            return;
        }

        if (respond.message === 'AbortError') {
            return;
        }

        if (respond.message === 'Error de conexión') {
            setError('Error de conexión');
            return;
        }

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
            setError('Ocurrió un error. Probá de nuevo.');
        }
    } catch (err) {
        if (err.name !== 'AbortError') {
            setError('Ocurrió un error. Probá de nuevo.');
        }
    } finally {
        if (controllerRef.current === controller) {
            controllerRef.current = null;
        }
        setIsDisabled(false);
    }
};

export const handleRegister = async ({
    username,
    password,
    verificationPassword,
    controllerRef,
    setIsDisabled,
    setError,
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

        if (!respond.ok) {
            const { detail } = await respond.json();
            setError(
                Array.isArray(detail)
                    ? detail.map((e) => (e.msg ?? '').replace(/^Value error,\s*/i, '')).join(' ')
                    : detail ?? 'Ocurrió un error. Probá de nuevo.',
            );
            return;
        }

        const login = await loginRequest({ username, password }, controller.signal);

        if (!login.ok) {
            if (login.message !== 'AbortError') {
                setError('Cuenta creada, pero no se pudo iniciar sesión. Iniciá sesión manualmente.');
            }
            return;
        }

        await refrescar();
    } catch (error) {
        if (error.name !== 'AbortError') {
            setError('Error de conexión');
        }
    } finally {
        if (controllerRef.current === controller) {
            controllerRef.current = null;
        }
        setIsDisabled(false);
    }
};