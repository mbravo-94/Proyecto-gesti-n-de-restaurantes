
// Función para agregar un producto al carrito
function agregarProducto(nombre, imgSrc, precio, cantidad) {
    // Obtener la tabla
    const tabla = document.getElementById('cartTable').getElementsByTagName('tbody')[0];

    // Crear una nueva fila
    const nuevaFila = tabla.insertRow();

    // Crear las celdas
    const celdaNombre = nuevaFila.insertCell(0);
    const celdaImagen = nuevaFila.insertCell(1);
    const celdaPrecio = nuevaFila.insertCell(2);
    const celdaCantidad = nuevaFila.insertCell(3);

    // Llenar las celdas con los datos
    celdaNombre.textContent = nombre;

    const img = document.createElement('img');
    img.src = imgSrc;
    celdaImagen.appendChild(img);

    celdaPrecio.textContent = `$${precio.toFixed(2)}`;
    celdaCantidad.textContent = cantidad;
}

// Ejemplo de uso de la función
agregarProducto("Camiseta", "https://via.placeholder.com/50", 19.99, 2);
agregarProducto("Zapatos", "https://via.placeholder.com/50", 49.99, 1);
agregarProducto("Gorra", "https://via.placeholder.com/50", 15.99, 3);
