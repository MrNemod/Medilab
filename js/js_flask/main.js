function getDiseases() {
    fetch('http://127.0.0.1:500/diseases')
        .then(response => {
            if (!response.ok) {
                throw new Error('Error en la solicitud: ' + response.status);
            }
            return response.json();
        })
        .then(data => {
            console.log('Datos de la API:', data);
        })
        .catch(error => {
            console.error('Hubo un problema con la solicitud:', error);
        });
}

// Ejecutar la función cuando la página se cargue completamente
window.onload = function() {
    getDiseases();
};
