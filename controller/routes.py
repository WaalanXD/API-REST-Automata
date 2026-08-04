# controller/routes.py
from flask import Blueprint, request, jsonify
from gateway.coordinator import process_conversion, process_simulation

# Creamos un Blueprint para agrupar estas rutas
controller_bp = Blueprint('controller', __name__)


@controller_bp.route('/convert', methods=['POST'])
def convert_nfa():
    # 1. Recibir los datos de entrada
    nfa_data = request.get_json()

    # 2. Validar que vengan datos (una validación básica de controlador)
    if not nfa_data:
        return jsonify({"error": "No JSON data provided"}), 400

    # 3. Pasar la responsabilidad al Gateway y retornar la respuesta
    response_data = process_conversion(nfa_data)
    return jsonify(response_data), 200


@controller_bp.route('/simulate', methods=['POST'])
def simulate_dfa():
    simulation_data = request.get_json()

    if not simulation_data:
        return jsonify({"error": "No JSON data provided"}), 400

    response_data = process_simulation(simulation_data)
    return jsonify(response_data), 200