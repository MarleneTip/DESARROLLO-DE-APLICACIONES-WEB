import sqlite3

def conectar():
    conexion = sqlite3.connect("tienda.db")
    return conexion


def crear_tablas():
    conexion = conectar()
    cursor = conexion.cursor()

    cursor.execute("""
        CREATE TABLE IF NOT EXISTS productos (
            id INTEGER PRIMARY KEY,
            nombre TEXT NOT NULL,
            cantidad INTEGER NOT NULL,
            precio REAL NOT NULL
        )
    """)

    conexion.commit()
    conexion.close()


def insertar_producto(id, nombre, cantidad, precio):
    conexion = conectar()
    cursor = conexion.cursor()

    cursor.execute("""
        INSERT INTO productos (id, nombre, cantidad, precio)
        VALUES (?, ?, ?, ?)
    """, (id, nombre, cantidad, precio))

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

    cursor.execute("DELETE FROM productos WHERE id = ?", (id_producto,))

    conexion.commit()
    conexion.close()


def actualizar_producto_db(id_producto, cantidad, precio):
    conexion = conectar()
    cursor = conexion.cursor()

    cursor.execute("""
        UPDATE productos
        SET cantidad = ?, precio = ?
        WHERE id = ?
    """, (cantidad, precio, id_producto))

    conexion.commit()
    conexion.close()

    import sqlite3

def obtener_producto(id_producto):
    conexion = sqlite3.connect("tienda.db")
    cursor = conexion.cursor()

    cursor.execute("SELECT * FROM productos WHERE id=?", (id_producto,))
    producto = cursor.fetchone()

    conexion.close()
    return producto


def actualizar_producto(id_producto, nombre, cantidad, precio):
    conexion = sqlite3.connect("tienda.db")
    cursor = conexion.cursor()

    cursor.execute("""
        UPDATE productos
        SET nombre=?, cantidad=?, precio=?
        WHERE id=?
    """, (nombre, cantidad, precio, id_producto))

    conexion.commit()
    conexion.close()