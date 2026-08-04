# app.py
from flask import Flask
from controller.routes import controller_bp

app = Flask(__name__)

# Registramos las rutas que creamos en el controlador
app.register_blueprint(controller_bp)

if __name__ == '__main__':
    # Arrancamos el servidor en el puerto 5000
    app.run(debug=True, port=5000)