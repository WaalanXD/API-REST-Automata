# controller/routes.py

from fastapi import APIRouter, HTTPException
from gateway.coordinator import AutomataGateway
#El router sirve para registrar las rutas de /convert y /simulate
router = APIRouter()


def _require_payload_field(payload: dict, field_name: str):
    if field_name not in payload:
        raise ValueError(f"Missing required field: {field_name}")

    value = payload[field_name]
    if value is None:
        raise ValueError(f"Missing required field: {field_name}")

    return value

@router.post("/convert")
def convert_nfa(payload: dict):
    """
    Ruta 1: Recibe el NFA en un diccionario/JSON y devuelve el DFA.
    """
    try:
        if not isinstance(payload, dict):
            raise ValueError("The request body must be a JSON object")

        _require_payload_field(payload, "states")
        _require_payload_field(payload, "alphabet")
        _require_payload_field(payload, "initial")
        _require_payload_field(payload, "accepting")
        _require_payload_field(payload, "transitions")

        resultado = AutomataGateway.process_conversion(payload)
        return resultado
    except Exception as e:
        raise HTTPException(status_code=400, detail=str(e))

@router.post("/simulate")
def simulate_dfa_endpoint(payload: dict):
    """
    Ruta 2: Recibe el DFA y la palabra a probar ('input_string').
    """
    try:
        if not isinstance(payload, dict):
            raise ValueError("The request body must be a JSON object")

        dfa = payload.get("dfa")
        cadena = payload.get("input_string")

        if dfa is None:
            raise ValueError("Missing required field: dfa")

        if cadena is None:
            raise ValueError("Missing required field: input_string")

        if not isinstance(dfa, dict):
            raise ValueError("The 'dfa' field must be a JSON object")

        if not isinstance(cadena, str):
            raise ValueError("The 'input_string' field must be a string")

        resultado = AutomataGateway.process_simulation(dfa, cadena)
        return resultado
    except Exception as e:
        raise HTTPException(status_code=400, detail=str(e))