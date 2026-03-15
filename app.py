from flask import Flask, render_template, request, redirect, flash, url_for
from database import obtener_productos, insertar_producto, insertar_usuario
from inventario import guardar_txt, guardar_json, guardar_csv
from database import obtener_producto, actualizar_producto

app = Flask(__name__)
app.secret_key = "clave_secreta"  # útil si luego agregas flash messages

# -------------------------
# Rutas existentes del proyecto
# -------------------------

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

# Editar producto
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

# Ver datos
@app.route("/datos")
def ver_datos():
    import json, csv

    with open("data/datos.txt") as archivo:
        datos_txt = archivo.readlines()

    with open("data/datos.json") as archivo:
        datos_json = json.load(archivo)

    datos_csv = []
    with open("data/datos.csv") as archivo:
        reader = csv.reader(archivo)
        for fila in reader:
            datos_csv.append(fila)

    return render_template("datos.html",
                           txt=datos_txt,
                           json=datos_json,
                           csv=datos_csv)

# Otras páginas
@app.route("/inicio")
def pagina_inicio():
    return render_template("inicio.html")

@app.route("/productos")
def pagina_productos():
    return render_template("productos.html")

@app.route("/about")
def pagina_about():
    return render_template("about.html")

@app.route("/contacto")
def pagina_contacto():
    return render_template("contacto.html")

# -------------------------
# NUEVAS RUTAS: Registro y prueba
# -------------------------

@app.route("/registro", methods=["GET", "POST"])
def registro():
    if request.method == "POST":
        nombre = request.form["nombre"]
        mail = request.form["mail"]
        password = request.form["password"]

        try:
            # Inserta el usuario en la base de datos
            insertar_usuario(nombre, mail, password)
            
            # Mensaje de éxito
            flash("Usuario registrado correctamente", "success")
            return redirect("/registro")
        except Exception as e:
            # Mensaje de error
            flash(f"Error al registrar usuario: {e}", "danger")
            return redirect("/registro")

    return render_template("registro.html")


@app.route("/prueba")
def prueba():
    return "Ruta funcionando"

# -------------------------
# Ejecutar la app
# -------------------------
if __name__ == "__main__":
    app.run(debug=True)