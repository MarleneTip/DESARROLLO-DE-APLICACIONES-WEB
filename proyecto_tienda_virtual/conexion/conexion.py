import mysql.connector

def obtener_conexion():
    conexion = mysql.connector.connect(
        host="crossover.proxy.rlwy.net",
        user="root",
        password="jdPUeMKJyKbjtzlOCaJKrFkvuUtrmiWg",
        database="railway",
        port=50852
    )
    return conexion