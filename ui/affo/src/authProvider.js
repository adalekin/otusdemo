import decodeJwt from 'jwt-decode';

const authProvider = {
    login: ({ username, password }) => {
        const request = new Request('http://affo.arch.homework/login/', {
            method: 'POST',
            body: JSON.stringify({ email: username, password }),
            headers: new Headers({ 'Content-Type': 'application/json' }),
        });
        return fetch(request)
            .then(response => {
                if (response.status < 200 || response.status >= 300) {
                    throw new Error(response.statusText);
                }
                return response.json();
            })
            .then(auth => {
                localStorage.setItem('auth', JSON.stringify(auth));
                return auth
            })
            .then(({ access_token }) => {
                const decodedToken = decodeJwt(access_token);
                localStorage.setItem('access_token', access_token);
                localStorage.setItem('permissions', decodedToken.permissions);
            })
            .catch(() => {
                throw new Error('Network error')
            });
    },
    checkError: (error) => {
        const status = error.status;
        if (status === 401 || status === 403) {
            localStorage.removeItem('auth');
            return Promise.reject();
        }
        // other error code (404, 500, etc): no need to log out
        return Promise.resolve();
    },
    checkAuth: () => localStorage.getItem('auth')
        ? Promise.resolve()
        : Promise.reject(),
    logout: () => {
        localStorage.removeItem('auth');
        localStorage.removeItem('access_token');
        localStorage.removeItem('permissions');
        return Promise.resolve();
    },
    getIdentity: () => {
        try {
            const { id, first_name, last_name } = JSON.parse(localStorage.getItem('auth'));
            return Promise.resolve({ id, fullName: `${first_name} ${last_name}`, avatar: null});
        } catch (error) {
            return Promise.reject(error);
        }
    },
    getPermissions: () => {
        const role = localStorage.getItem('permissions');
        return role ? Promise.resolve(role) : Promise.reject();
    }
};

export default authProvider;
