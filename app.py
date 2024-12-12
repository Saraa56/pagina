import os
from flask import Flask
from routes.Comentarios_routes import comentarios_bp
from routes.cliente_routes import cliente_bp
from routes.compra_routes import compra_bp
from routes.devolucion_routes import devolucion_bp
from routes.producto_routes import producto_bp
from routes.sucursal_routes import sucursal_bp

# Configuración del entorno
os.environ["FLASK_ENV"] = "development"  # Activar modo de desarrollo

def create_app():
    app = Flask(__name__)

    # Registrar los blueprints
    app.register_blueprint(comentarios_bp)
    app.register_blueprint(cliente_bp, url_prefix='/api')
    app.register_blueprint(compra_bp, url_prefix='/api')
    app.register_blueprint(devolucion_bp, url_prefix='/api')
    app.register_blueprint(producto_bp, url_prefix='/api')
    app.register_blueprint(sucursal_bp, url_prefix='/api')

    return app

if __name__ == "__main__":
    # Crear la aplicación y ejecutarla en modo depuración
    app = create_app()
    app.run(debug=True)
