from flask import Flask, render_template, request, redirect, flash, url_for

from flask_login import LoginManager, UserMixin, login_user, logout_user, login_required, current_user

from services.producto_service import (
    listar_productos,
    crear_producto,
    editar_producto,
    borrar_producto,
    buscar_usuario
)

from models.database import obtener_producto, obtener_productos, conectar 
from reportlab.pdfgen import canvas
from io import BytesIO
from flask import make_response

ADMIN_EMAIL = "marlenetip.mimi@gmail.com"

# Crear app
app = Flask(__name__)
app.secret_key = "clave_secreta"

# Configuración Flask-Login
login_manager = LoginManager()
login_manager.init_app(app)
login_manager.login_view = "login"
login_manager.login_message = "Debes iniciar sesión"
# Modelo de usuario
class Usuario(UserMixin):
    def __init__(self, id, nombre, email, password):
        self.id = str(id)
        self.nombre = nombre
        self.email = email
        self.password = password

# Cargar usuario desde la BD
@login_manager.user_loader
def load_user(user_id):
    conexion = conectar()
    cursor = conexion.cursor()

    cursor.execute(
        "SELECT * FROM usuarios WHERE id_usuario = %s",
        (int(user_id),)
    )
    user = cursor.fetchone()

    conexion.close()

    if user:
        return Usuario(user[0], user[1], user[2], user[3])
    return None


# -------------------------
# Rutas existentes del proyecto
# -------------------------

# Página principal
@app.route("/")
def inicio():
    return render_template("index.html")

# Mostrar inventario
@app.route("/inventario")
@login_required
def inventario():
    productos = listar_productos()
    return render_template("inventario.html", productos=productos)

@app.route("/agregar", methods=["GET", "POST"])
@login_required
def agregar():
    if current_user.email != ADMIN_EMAIL:
        return redirect("/inventario")

    if request.method == "POST":
        nombre = request.form["nombre"]
        cantidad = request.form["cantidad"]
        precio = request.form["precio"]

        crear_producto(nombre, cantidad, precio)

        return redirect("/inventario")

    return render_template("agregar.html")

# Editar producto
@app.route("/editar/<id>", methods=["GET", "POST"])
@login_required
def editar(id):
    if current_user.email != ADMIN_EMAIL:
        return redirect("/inventario")

    if request.method == "POST":
        nombre = request.form["nombre"]
        cantidad = request.form["cantidad"]
        precio = request.form["precio"]

        editar_producto(id, nombre, cantidad, precio)
        return redirect("/inventario")

    producto = obtener_producto(id)
    return render_template("editar.html", producto=producto)

# Ver datos
@app.route("/datos")
@login_required
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

@app.route("/productos")
def pagina_productos():
    productos = obtener_productos()
    return render_template("productos.html", productos=productos)

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
        nombre = request.form.get("nombre")
        email = request.form.get("email")
        password = request.form.get("password")

        print(request.form)

        try:
            conexion = conectar()
            cursor = conexion.cursor()

            cursor.execute(
                "INSERT INTO usuarios (nombre, email, password) VALUES (%s, %s, %s)",
                (nombre, email, password)
            )

            conexion.commit()
            conexion.close()

            flash("Usuario registrado correctamente", "success")
            return redirect("/login")

        except Exception as e:
            flash(f"Error: {e}", "danger")
            return redirect("/registro")

    return render_template("registro.html")

@app.route("/prueba")
def prueba():
    return "Ruta funcionando"

@app.route("/login", methods=["GET", "POST"])
def login():
    if request.method == "POST":
        email = request.form.get("email")
        password = request.form.get("password")

        # buscar usuario desde service
        user = buscar_usuario(email)

        print("USUARIO:", user)
        print("PASSWORD INGRESADO:", password)

        if user and user[3] == password:
            usuario = Usuario(user[0], user[1], user[2], user[3])
            login_user(usuario)
            print("LOGIN EXITOSO")
            return redirect("/")
        else:
            print("LOGIN FALLÓ")
            flash("Correo o contraseña incorrectos")

    return render_template("login.html")

@app.route("/logout")
@login_required
def logout():
    logout_user()
    return redirect("/login")

@app.route("/carrito")
@login_required
def ver_carrito():
    carrito = request.args.getlist("producto")
    return render_template("carrito.html", carrito=carrito)

@app.route("/finalizar_compra")
@login_required
def finalizar_compra():
    return render_template("compra_exitosa.html")

@app.route("/eliminar/<id>")
@login_required
def eliminar(id):
    if current_user.email != ADMIN_EMAIL:
        return redirect("/inventario")

    borrar_producto(id)
    return redirect("/inventario")

@app.route("/reporte/pdf")
@login_required
def generar_pdf():

    productos = listar_productos()

    buffer = BytesIO()
    pdf = canvas.Canvas(buffer)

    pdf.drawString(100, 800, "REPORTE DE PRODUCTOS")

    y = 750
    for p in productos:
        pdf.drawString(100, y, f"{p}")
        y -= 20

    pdf.save()

    buffer.seek(0)

    return make_response(buffer.getvalue(), {
        "Content-Type": "application/pdf",
        "Content-Disposition": "inline; filename=reporte.pdf"
    })

# -------------------------
# Ejecutar la app
# -------------------------
if __name__ == "__main__":
    app.run(debug=True)
