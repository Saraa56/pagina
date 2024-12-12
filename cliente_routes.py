from flask import Blueprint, request, jsonify
from models.cliente import crear_cliente, obtener_clientes, obtener_cliente_por_id, actualizar_cliente, eliminar_cliente

cliente_bp = Blueprint('cliente', __name__)

# Crear un nuevo cliente
@cliente_bp.route('/clientes', methods=['POST'])
def agregar_cliente():
    data = request.get_json()
    nombre = data['nombre']
    correo = data['correo']
    telefono = data['telefono']
    Direccion = data['Direccion']
    latitud = data['latitud']
    longitud = data['longitud']
    
    crear_cliente(nombre, correo, telefono, Direccion, latitud, longitud)
    return jsonify({"message": "Cliente registrado con éxito"}), 201

# Obtener todos los clientes
@cliente_bp.route('/clientes', methods=['GET'])
def obtener_todos_los_clientes():
    clientes = obtener_clientes()
    return jsonify(clientes)

# Obtener un cliente por ID
@cliente_bp.route('/clientes/<int:cliente_id>', methods=['GET'])
def obtener_cliente(cliente_id):
    cliente = obtener_cliente_por_id(cliente_id)
    if cliente:
        return jsonify(cliente)
    return jsonify({"message": "Cliente no encontrado"}), 404

# Actualizar un cliente
@cliente_bp.route('/clientes/<int:cliente_id>', methods=['PUT'])
def actualizar_cliente_info(cliente_id):
    data = request.get_json()
    nombre = data['nombre']
    correo = data['correo']
    telefono = data['telefono']
    Direccion = data['Direccion']
    latitud = data['latitud']
    longitud = data['longitud']
    
    actualizar_cliente(cliente_id, nombre, correo, telefono, Direccion, latitud, longitud)
    return jsonify({"message": "Cliente actualizado con éxito"})

# Eliminar un cliente
@cliente_bp.route('/clientes/<int:cliente_id>', methods=['DELETE'])
def eliminar_cliente_info(cliente_id):
    eliminar_cliente(cliente_id)
    return jsonify({"message": "Cliente eliminado con éxito"})
