from flask import Blueprint, request, jsonify
from models.producto import crear_producto, obtener_productos

producto_bp = Blueprint('producto', __name__)

# Crear un nuevo producto
@producto_bp.route('/productos', methods=['POST'])
def agregar_producto():
    data = request.get_json()
    try:
        # Asegúrate de que los datos existan y sean correctos
        nombre = data['nombre']
        precio = data['precio']
        stock = data['stock']
        
        # Llamar a la función para agregar el producto
        crear_producto(nombre, precio, stock)
        return jsonify({"message": "Producto agregado con éxito"}), 201
    except KeyError as e:
        return jsonify({"error": f"Faltan campos: {str(e)}"}), 400
    except Exception as e:
        return jsonify({"error": str(e)}), 500

# Obtener todos los productos
@producto_bp.route('/productos', methods=['GET'])
def obtener_todos_los_productos():
    try:
        productos = obtener_productos()
        return jsonify(productos), 200
    except Exception as e:
        return jsonify({"error": str(e)}), 500
