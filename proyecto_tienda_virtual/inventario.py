class Producto:
    def __init__(self, id_producto, nombre, cantidad, precio):
        self.__id = id_producto
        self.__nombre = nombre
        self.__cantidad = cantidad
        self.__precio = precio

    # Métodos GET
    def get_id(self):
        return self.__id

    def get_nombre(self):
        return self.__nombre

    def get_cantidad(self):
        return self.__cantidad

    def get_precio(self):
        return self.__precio

    # Métodos SET
    def set_nombre(self, nombre):
        self.__nombre = nombre

    def set_cantidad(self, cantidad):
        self.__cantidad = cantidad

    def set_precio(self, precio):
        self.__precio = precio

    def __str__(self):
        return f"ID: {self.__id} | Nombre: {self.__nombre} | Cantidad: {self.__cantidad} | Precio: ${self.__precio}"
    class Inventario:
    def __init__(self):
        # Diccionario donde:
        # clave = id del producto
        # valor = objeto Producto
        self.productos = {}

    # Añadir producto
    def agregar_producto(self, producto):
        if producto.get_id() in self.productos:
            print("El producto ya existe.")
        else:
            self.productos[producto.get_id()] = producto
            print("Producto agregado correctamente.")

    # Eliminar producto por ID
    def eliminar_producto(self, id_producto):
        if id_producto in self.productos:
            del self.productos[id_producto]
            print("Producto eliminado correctamente.")
        else:
            print("Producto no encontrado.")

    # Actualizar cantidad
    def actualizar_cantidad(self, id_producto, nueva_cantidad):
        if id_producto in self.productos:
            self.productos[id_producto].set_cantidad(nueva_cantidad)
            print("Cantidad actualizada.")
        else:
            print("Producto no encontrado.")

    # Actualizar precio
    def actualizar_precio(self, id_producto, nuevo_precio):
        if id_producto in self.productos:
            self.productos[id_producto].set_precio(nuevo_precio)
            print("Precio actualizado.")
        else:
            print("Producto no encontrado.")

    # Buscar producto por nombre
    def buscar_por_nombre(self, nombre):
        encontrados = []
        for producto in self.productos.values():
            if nombre.lower() in producto.get_nombre().lower():
                encontrados.append(producto)
        return encontrados

    # Mostrar todos los productos
    def mostrar_todos(self):
        return list(self.productos.values())
    @app.route("/agregar", methods=["GET", "POST"])
def agregar():
    if request.method == "POST":
        id_producto = request.form["id"]
        nombre = request.form["nombre"]
        cantidad = request.form["cantidad"]
        precio = request.form["precio"]

        insertar_producto(id_producto, nombre, cantidad, precio)

        return redirect("/inventario")

    return render_template("agregar.html")