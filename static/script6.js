const formulario = document.getElementById('formulario');

const nombre = document.getElementById('nombre');
const correo = document.getElementById('correo');
const password = document.getElementById('password');
const confirmar = document.getElementById('confirmar');
const edad = document.getElementById('edad');

const btnEnviar = document.getElementById('btn-enviar');

const errorNombre = document.getElementById('error-nombre');
const errorCorreo = document.getElementById('error-correo');
const errorPassword = document.getElementById('error-password');
const errorConfirmar = document.getElementById('error-confirmar');
const errorEdad = document.getElementById('error-edad');
function validarNombre() {
    if (nombre.value.trim().length < 3) {
        errorNombre.textContent = 'El nombre debe tener al menos 3 caracteres';
        nombre.classList.add('invalido');
        nombre.classList.remove('valido');
        return false;
    } else {
        errorNombre.textContent = '';
        nombre.classList.add('valido');
        nombre.classList.remove('invalido');
        return true;
    }
}
function validarCorreo() {
    const regexCorreo = /^[^\s@]+@[^\s@]+\.[^\s@]+$/;

    if (!regexCorreo.test(correo.value)) {
        errorCorreo.textContent = 'Ingrese un correo electrónico válido';
        correo.classList.add('invalido');
        correo.classList.remove('valido');
        return false;
    } else {
        errorCorreo.textContent = '';
        correo.classList.add('valido');
        correo.classList.remove('invalido');
        return true;
    }
}
correo.addEventListener('input', validarCorreo);
function validarPassword() {
    const regexPassword = /^(?=.*[0-9])(?=.*[!@#$%^&*])/;

    if (password.value.length < 8 || !regexPassword.test(password.value)) {
        errorPassword.textContent = 'Mínimo 8 caracteres, un número y un carácter especial';
        password.classList.add('invalido');
        password.classList.remove('valido');
        return false;
    } else {
        errorPassword.textContent = '';
        password.classList.add('valido');
        password.classList.remove('invalido');
        return true;
    }
}
password.addEventListener('input', validarPassword);
function validarConfirmacion() {
    if (confirmar.value !== password.value || confirmar.value === '') {
        errorConfirmar.textContent = 'Las contraseñas no coinciden';
        confirmar.classList.add('invalido');
        confirmar.classList.remove('valido');
        return false;
    } else {
        errorConfirmar.textContent = '';
        confirmar.classList.add('valido');
        confirmar.classList.remove('invalido');
        return true;
    }
}
confirmar.addEventListener('input', validarConfirmacion);
password.addEventListener('input', validarConfirmacion);
function validarEdad() {
    if (edad.value === '' || parseInt(edad.value) < 18) {
        errorEdad.textContent = 'Debes ser mayor o igual a 18 años';
        edad.classList.add('invalido');
        edad.classList.remove('valido');
        return false;
    } else {
        errorEdad.textContent = '';
        edad.classList.add('valido');
        edad.classList.remove('invalido');
        return true;
    }
}
edad.addEventListener('input', validarEdad);
function validarFormulario() {
    const esValido =
        validarNombre() &&
        validarCorreo() &&
        validarPassword() &&
        validarConfirmacion() &&
        validarEdad();

    btnEnviar.disabled = !esValido;
}
nombre.addEventListener('input', validarFormulario);
correo.addEventListener('input', validarFormulario);
password.addEventListener('input', validarFormulario);
confirmar.addEventListener('input', validarFormulario);
edad.addEventListener('input', validarFormulario);
formulario.addEventListener('submit', function (e) {
    e.preventDefault();

    if (
        validarNombre() &&
        validarCorreo() &&
        validarPassword() &&
        validarConfirmacion() &&
        validarEdad()
    ) {
        alert('Formulario validado correctamente');
        formulario.reset();
        btnEnviar.disabled = true;

        const inputs = document.querySelectorAll('input');
        inputs.forEach(input => {
            input.classList.remove('valido', 'invalido');
        });
    }
});
