from flask import Flask, render_template, request, redirect
from database import crear_tablas, obtener_productos, insertar_producto
from inventario import guardar_txt, guardar_json, guardar_csv
from database import obtener_producto, actualizar_producto
app = Flask(__name__)

# Crear tabla automáticamente al iniciar
crear_tablas()


# Página principal
@app.route("/")
def inicio():
    return redirect("/inventario")


# Mostrar inventario
@app.route("/inventario")
def ver_inventario():
    productos = obtener_productos()
    return render_template("inventario.html", productos=productos)


# Agregar productos
@app.route("/agregar", methods=["GET", "POST"])
def agregar():
    if request.method == "POST":
        id_producto = request.form["id"]
        nombre = request.form["nombre"]
        cantidad = request.form["cantidad"]
        precio = request.form["precio"]

        insertar_producto(id_producto, nombre, cantidad, precio)

        guardar_txt(nombre, precio, cantidad)
        guardar_json(nombre, precio, cantidad)
        guardar_csv(nombre, precio, cantidad)

        return redirect("/inventario")

    return render_template("agregar.html")

@app.route("/editar/<id>", methods=["GET", "POST"])
def editar(id):

    if request.method == "POST":
        nombre = request.form["nombre"]
        cantidad = request.form["cantidad"]
        precio = request.form["precio"]

        actualizar_producto(id, nombre, cantidad, precio)

        return redirect("/inventario")

    producto = obtener_producto(id)

    return render_template("editar.html", producto=producto)
@app.route("/datos")
def ver_datos():

    with open("data/datos.txt") as archivo:
        datos_txt = archivo.readlines()

    import json
    with open("data/datos.json") as archivo:
        datos_json = json.load(archivo)

    import csv
    datos_csv = []
    with open("data/datos.csv") as archivo:
        reader = csv.reader(archivo)
        for fila in reader:
            datos_csv.append(fila)

    return render_template("datos.html",
                           txt=datos_txt,
                           json=datos_json,
                           csv=datos_csv)
if __name__ == "__main__":
    app.run(debug=True)