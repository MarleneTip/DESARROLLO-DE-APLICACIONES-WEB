from models.database import conectar

class Producto:

    def __init__(self, id=None, nombre=None, cantidad=None, precio=None):
        self.id = id
        self.nombre = nombre
        self.cantidad = cantidad
        self.precio = precio

    @staticmethod
    def obtener_todos():
        conexion = conectar()
        cursor = conexion.cursor(dictionary=True)

        cursor.execute("SELECT * FROM productos")
        datos = cursor.fetchall()

        cursor.close()
        conexion.close()

        return datos

    @staticmethod
    def insertar(nombre, cantidad, precio):
        conexion = conectar()
        cursor = conexion.cursor()

        sql = "INSERT INTO productos (nombre, cantidad, precio) VALUES (%s, %s, %s)"
        cursor.execute(sql, (nombre, cantidad, precio))

        conexion.commit()

        cursor.close()
        conexion.close()

    @staticmethod
    def eliminar(id):
        conexion = conectar()
        cursor = conexion.cursor()

        cursor.execute("DELETE FROM productos WHERE id=%s", (id,))
        conexion.commit()

        cursor.close()
        conexion.close()