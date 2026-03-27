import mysql.connector

def obtener_conexion():
    conexion = mysql.connector.connect(
        host="mysql.railway.internal",
        user="root",
        password="jdPUeMKJyKbjtzlOCaJKrFkvuUtrmiWg",
        database="railway"
        port=3306
    )
    return conexion