from conexion.conexion import obtener_conexion


def conectar():
    return obtener_conexion()


def insertar_producto(nombre, cantidad, precio):
    conexion = conectar()
    cursor = conexion.cursor()

    cursor.execute("""
        INSERT INTO productos (nombre, cantidad, precio)
        VALUES (%s, %s, %s)
    """, (nombre, cantidad, precio))

    conexion.commit()
    conexion.close()


def obtener_productos():
    conexion = conectar()
    cursor = conexion.cursor()

    cursor.execute("SELECT * FROM productos")
    productos = cursor.fetchall()

    conexion.close()
    return productos


def eliminar_producto_db(id_producto):
    conexion = conectar()
    cursor = conexion.cursor()

    cursor.execute("DELETE FROM productos WHERE id_producto=%s", (id_producto,))

    conexion.commit()
    conexion.close()


def obtener_producto(id_producto):
    conexion = conectar()
    cursor = conexion.cursor()

    cursor.execute("SELECT * FROM productos WHERE id_producto=%s", (id_producto,))
    producto = cursor.fetchone()

    conexion.close()
    return producto

def eliminar_producto(id):
    conexion = conectar()
    cursor = conexion.cursor()

    cursor.execute("DELETE FROM productos WHERE id_producto = %s", (id,))
    
    conexion.commit()
    conexion.close()

def actualizar_producto(id_producto, nombre, cantidad, precio):
    conexion = conectar()
    cursor = conexion.cursor()

    cursor.execute("""
        UPDATE productos
        SET nombre=%s, cantidad=%s, precio=%s
        WHERE id_producto=%s
    """, (nombre, cantidad, precio, id_producto))

    conexion.commit()
    conexion.close()
def insertar_usuario(nombre, mail, password):
    conexion = conectar()
    cursor = conexion.cursor()

    cursor.execute("""
        INSERT INTO usuarios (nombre, mail, password)
        VALUES (%s, %s, %s)
    """, (nombre, mail, password))

    conexion.commit()
    conexion.close()