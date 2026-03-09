import json

class Producto:
    def __init__(self, id_producto, nombre, cantidad, precio):
        self.__id = id_producto
        self.__nombre = nombre
        self.__cantidad = cantidad
        self.__precio = precio

    def get_id(self):
        return self.__id

    def get_nombre(self):
        return self.__nombre

    def get_cantidad(self):
        return self.__cantidad

    def get_precio(self):
        return self.__precio

    def set_precio(self, precio):
        self.__precio = precio

    def __str__(self):
        return f"ID: {self.__id} | Nombre: {self.__nombre} | Cantidad: {self.__cantidad} | Precio: ${self.__precio}"


class Inventario:

    def __init__(self):
        self.productos = {}

    def agregar_producto(self, producto):
        if producto.get_id() in self.productos:
            print("El producto ya existe.")
        else:
            self.productos[producto.get_id()] = producto
            print("Producto agregado correctamente.")

    def eliminar_producto(self, id_producto):
        if id_producto in self.productos:
            del self.productos[id_producto]
            print("Producto eliminado correctamente.")
        else:
            print("Producto no encontrado.")

    def mostrar_todos(self):
        return list(self.productos.values())


# ---------- FUNCIONES DE PERSISTENCIA ----------

def guardar_txt(nombre, precio, cantidad):

    with open("data/datos.txt", "a") as archivo:
        linea = f"{nombre},{precio},{cantidad}\n"
        archivo.write(linea)


def leer_txt():

    with open("data/datos.txt", "r") as archivo:
        datos = archivo.readlines()

    return datos


def guardar_json(nombre, precio, cantidad):

    producto = {
        "nombre": nombre,
        "precio": precio,
        "cantidad": cantidad
    }

    try:
        with open("data/datos.json", "r") as archivo:
            datos = json.load(archivo)
    except:
        datos = []

    datos.append(producto)

    with open("data/datos.json", "w") as archivo:
        json.dump(datos, archivo, indent=4)

        import csv

def guardar_csv(nombre, precio, cantidad):

    with open("inventario/data/datos.csv", "a", newline="") as archivo:

        writer = csv.writer(archivo)

        writer.writerow([nombre, precio, cantidad])