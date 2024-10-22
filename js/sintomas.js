const selectedDiseases = new Set();
let symptomsCount = 0;
let symptomsList = [];
let symptoms = []; // Almacena todos los síntomas

async function loadSyntom() {
    try {
        const response = await fetch('http://127.0.0.1:5000/symptoms');
        if (!response.ok) {
            throw new Error('Error en la respuesta de la API');
        }
        
        symptoms = await response.json(); // Almacena todos los síntomas

        const categories = {};
        symptoms.forEach(syntom => {
            const partOfBody = syntom.parte_del_cuerpo || "Otros";
            if (!categories[partOfBody]) {
                categories[partOfBody] = [];
            }
            categories[partOfBody].push(syntom);
        });

        const symptomsSelectContainer = document.getElementById('symptoms-select');
        for (const part in categories) {
            const label = document.createElement('label');
            label.textContent = part;
            symptomsSelectContainer.appendChild(label);

            const select = document.createElement('select');
            select.onchange = function() { addDisease(this); };
            select.id = part.replace(/\s+/g, '-').toLowerCase(); 
            select.innerHTML = '<option value="">Selecciona un síntoma</option>';

            categories[part].forEach(disease => {
                const option = document.createElement('option');
                option.value = disease.id;
                option.textContent = disease.nombre;
                select.appendChild(option);
            });

            symptomsSelectContainer.appendChild(select);
        }

        symptomsCount = symptoms.length; 
        symptomsList = Array(symptomsCount).fill(0);
        console.log('Lista de síntomas:', symptomsList);

    } catch (error) {
        console.error('Error al cargar los síntomas:', error);
        alert('Error al cargar los síntomas. Por favor, intenta de nuevo más tarde.');
    }
}

function addDisease(selectElement) {
    const diseaseId = selectElement.value;
    const diseaseName = selectElement.options[selectElement.selectedIndex].text;

    if (diseaseId && !selectedDiseases.has(diseaseId)) {
        selectedDiseases.add(diseaseId);
        const infoBox = document.getElementById('info-box');
        
        const diseaseItem = document.createElement('div');
        diseaseItem.classList.add('disease-item');
        diseaseItem.textContent = diseaseName;

        const removeButton = document.createElement('button'); 
        removeButton.textContent = 'Eliminar';
        removeButton.onclick = function () {
            selectedDiseases.delete(diseaseId);
            infoBox.removeChild(diseaseItem);

            const diseaseIndex = parseInt(diseaseId) - 1;
            symptomsList[diseaseIndex] = 0; 
            console.log('Lista de síntomas actualizada:', symptomsList);
        };

        diseaseItem.appendChild(removeButton);
        infoBox.appendChild(diseaseItem);

        const diseaseIndex = parseInt(diseaseId) - 1;
        symptomsList[diseaseIndex] = 1;
        console.log('Lista de síntomas actualizada:', symptomsList);

        selectElement.selectedIndex = 0;
    }
}

// Filtrado de síntomas para autocompletar
function filterSymptoms() {
    const input = document.getElementById('search-input');
    const filter = input.value.toLowerCase();
    const suggestionsContainer = document.getElementById('autocomplete-suggestions');

    // Limpiar sugerencias anteriores
    suggestionsContainer.innerHTML = '';

    if (filter.length === 0) {
        return; // Si no hay entrada, no mostrar sugerencias
    }

    const filteredSymptoms = symptoms.filter(syntom => 
        syntom.nombre.toLowerCase().includes(filter)
    );

    filteredSymptoms.forEach(syntom => {
        const suggestionItem = document.createElement('div');
        suggestionItem.textContent = syntom.nombre;
        suggestionItem.onclick = function () {
            selectSymptom(syntom); // Función para manejar la selección
            input.value = ''; // Limpiar el campo de búsqueda
            suggestionsContainer.innerHTML = ''; // Limpiar las sugerencias
        };
        suggestionsContainer.appendChild(suggestionItem);
    });
}

function selectSymptom(syntom) {
    const selectElement = document.getElementById(syntom.parte_del_cuerpo.replace(/\s+/g, '-').toLowerCase());
    const option = Array.from(selectElement.options).find(opt => opt.textContent === syntom.nombre);
    if (option) {
        option.selected = true; // Seleccionar el síntoma en el selector
        addDisease(selectElement); // Llama a la función para manejar la selección
    }
}

// Cambia la función llamada al cargar la página
window.onload = loadSyntom;


// Función para enviar symptomsList al servidor Flask
async function sendSymptomsList() {
    try {
        const response = await fetch('http://127.0.0.1:5000/prediction', {
            method: 'POST',
            headers: {
                'Content-Type': 'application/json',
            },
            body: JSON.stringify(symptomsList), // Enviar la lista de síntomas seleccionados
        });

        if (!response.ok) {
            throw new Error('Error al enviar la lista de síntomas');
        }

        const result = await response.json();
        console.log('Respuesta del servidor:', result);
        alert('Predicción recibida: ' + result.prediction);

    } catch (error) {
        console.error('Error al enviar la lista de síntomas:', error);
        alert('Error al enviar la lista de síntomas. Por favor, intenta de nuevo más tarde.');
    }
}

// Asignar la función al botón "Siguiente"
document.querySelector('.next-button').onclick = function() {
    sendSymptomsList();
};
