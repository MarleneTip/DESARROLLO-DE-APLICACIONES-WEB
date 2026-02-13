from flask import Flask

app = Flask(__name__)

@app.route('/')
def inicio():
    return "Bienvenido a la tienda virtual de Cucharitas Sorpresas"

@app.route('/producto/<nombre>')
def producto(nombre):
    return f"Producto: {nombre} disponible en Cucharitas Sorpresas"

if __name__ == '__main__':
    app.run(debug=True)
