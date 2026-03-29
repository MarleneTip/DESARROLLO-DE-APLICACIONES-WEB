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

from models.database import conectar

def buscar_usuario(email):
    conexion = conectar()
    cursor = conexion.cursor()

    cursor.execute("SELECT * FROM usuarios WHERE email = %s", (email,))
    usuario = cursor.fetchone()

    # esto evita el error de "Unread result"
    cursor.fetchall()

    cursor.close()
    conexion.close()

    return usuario