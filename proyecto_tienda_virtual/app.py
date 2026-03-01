from flask import Flask, render_template, request, redirect
from database import crear_tablas, obtener_productos, insertar_producto

app = Flask(__name__)

# Crear tabla automáticamente al iniciar
crear_tablas()


@app.route("/")
def inicio():
    return "Bienvenida a la tienda virtual de Cucharas Sorpresa 💄🥄"


@app.route("/inventario")
def ver_inventario():
    productos = obtener_productos()
    return render_template("inventario.html", productos=productos)


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


if __name__ == "__main__":
    app.run(debug=True)