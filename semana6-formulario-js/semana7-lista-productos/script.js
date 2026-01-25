// Arreglo de productos
const productos = [
    {
        nombre: "Laptop",
        precio: 950,
        descripcion: "Laptop para estudio y trabajo"
    },
    {
        nombre: "Mouse",
        precio: 32,
        descripcion: "Mouse inalámbrico"
    },
    {
        nombre: "Teclado",
        precio: 55,
        descripcion: "Teclado mecánico"
    }
];
// Obtener el elemento <ul> del HTML
const lista = document.getElementById("listaProductos");

// Función para renderizar los productos
function renderizarProductos() {
    // Limpiar la lista antes de renderizar
    lista.innerHTML = "";

    // Recorrer el arreglo de productos
    productos.forEach(producto => {
        const li = document.createElement("li");
        li.innerHTML = `
            <strong>${producto.nombre}</strong><br>
            Precio: $${producto.precio}<br>
            ${producto.descripcion}
        `;
        lista.appendChild(li);
    });
}

// Llamar a la función al cargar la página
renderizarProductos();
// Obtener el botón
const btnAgregar = document.getElementById("btnAgregar");

// Evento click del botón
btnAgregar.addEventListener("click", () => {
    const nuevoProducto = {
        nombre: "Nuevo Producto",
        precio: 60,
        descripcion: "Producto agregado dinámicamente"
    };

    // Agregar el producto al arreglo
    productos.push(nuevoProducto);

    // Volver a renderizar la lista
    renderizarProductos();
});
