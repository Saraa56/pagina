# app/routes/sucursal_routes.py

from flask import Blueprint, request, jsonify
from models.sucursal import crear_sucursal, obtener_sucursales

sucursal_bp = Blueprint('sucursal', __name__)

# Crear una nueva sucursal
@sucursal_bp.route('/sucursales', methods=['POST'])
def agregar_sucursal():
    data = request.get_json()
    nombre = data['nombre']
    latitud = data['latitud']
    longitud = data['longitud']
    
    crear_sucursal(nombre, latitud, longitud)
    return jsonify({"message": "Sucursal registrada con éxito"}), 201

# Obtener todas las sucursales
@sucursal_bp.route('/sucursales', methods=['GET'])
def obtener_todas_las_sucursales():
    sucursales = obtener_sucursales()
    return jsonify(sucursales)
