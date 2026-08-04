# controller/routes.py

from fastapi import APIRouter, HTTPException
from gateway.coordinator import AutomataGateway

# El router sirve para registrar las rutas /convert y /simulate
router = APIRouter()

@router.post("/convert")
def convert_nfa(payload: dict):
    """
    Ruta 1: Recibe el AFN en un diccionario/JSON y devuelve el AFD.
    """
    try:
        resultado = AutomataGateway.process_conversion(payload)
        return resultado
    except Exception as e:
        raise HTTPException(status_code=400, detail=str(e))

@router.post("/simulate")
def simulate_dfa_endpoint(payload: dict):
    """
    Ruta 2: Recibe el AFD y la palabra a probar ('input_string').
    """
    try:
        dfa = payload.get("dfa")
        cadena = payload.get("input_string")

        if dfa is None or cadena is None:
            raise ValueError("Falta enviar el 'dfa' o el 'input_string' en el JSON")

        resultado = AutomataGateway.process_simulation(dfa, cadena)
        return resultado
    except Exception as e:
        raise HTTPException(status_code=400, detail=str(e))