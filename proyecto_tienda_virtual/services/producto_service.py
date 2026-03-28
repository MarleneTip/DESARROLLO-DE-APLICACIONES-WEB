from models.database import (
    obtener_productos,
    insertar_producto,
    obtener_producto,
    actualizar_producto,
    eliminar_producto
)

def listar_productos():
    return obtener_productos()

def crear_producto(nombre, cantidad, precio):
    return insertar_producto(nombre, cantidad, precio)

def editar_producto(id, nombre, cantidad, precio):
    return actualizar_producto(id, nombre, cantidad, precio)

def borrar_producto(id):
    return eliminar_producto(id)