// Obtén los elementos
var modal = document.getElementById("terms-modal");
var btn = document.getElementById("start-checkup");
var span = document.getElementsByClassName("close")[0];
var form = document.getElementById("terms-form");
var contactLink = "contact"; // Enlace al que se redirigirá

// Abre la ventana modal
btn.onclick = function(event) {
    event.preventDefault(); // Evita que el enlace haga su acción predeterminada
    modal.style.display = "block";
}

// Cierra la ventana modal
span.onclick = function() {
    modal.style.display = "none";
}

// Envía el formulario
form.onsubmit = function(event) {
    event.preventDefault(); // Evita el envío del formulario
    var ageChecked = document.getElementById("age").checked;
    var infoChecked = document.getElementById("info-use").checked;

    if (ageChecked && infoChecked) {
        modal.style.display = "none";
        window.location.href = "../chequeo.html"; // Redirige al contacto
    } else {
        alert("Por favor, acepte todos los términos para continuar.");
    }
}

// Cierra la ventana modal si se hace clic fuera de ella
window.onclick = function(event) {
    if (event.target == modal) {
        modal.style.display = "none";
    }
}
