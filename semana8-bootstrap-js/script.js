document.getElementById("contactoForm").addEventListener("submit", function (event) {
    event.preventDefault();

    const nombre = document.getElementById("nombre").value.trim();
    const correo = document.getElementById("correo").value.trim();
    const mensaje = document.getElementById("mensaje").value.trim();

    if (nombre === "") {
        alert("Por favor, ingresa tu nombre.");
        return;
    }

    if (correo === "") {
        alert("Por favor, ingresa tu correo.");
        return;
    }

    const correoValido = /^[^\s@]+@[^\s@]+\.[^\s@]+$/;
    if (!correoValido.test(correo)) {
        alert("Ingresa un correo electrónico válido.");
        return;
    }

    if (mensaje === "") {
        alert("Por favor, escribe un mensaje.");
        return;
    }

    alert("Formulario enviado correctamente ✅");
});
document.getElementById("btnAlerta").addEventListener("click", function () {
    alert("¡Gracias por visitar mi proyecto de la Semana 8! 🚀");
});
