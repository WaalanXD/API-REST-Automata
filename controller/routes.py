# controller/routes.py

from fastapi import APIRouter, HTTPException
from gateway.coordinator import AutomataGateway
# El router sirve para registrar las rutas de /convert y /simulate.
router = APIRouter()


def _requerir_campo_payload(carga: dict, nombre_campo: str):
    if nombre_campo not in carga:
        raise ValueError(f"Missing required field: {nombre_campo}")

    valor = carga[nombre_campo]
    if valor is None:
        raise ValueError(f"Missing required field: {nombre_campo}")

    return valor

@router.post("/convert")
def convertir_nfa(carga: dict):
    """
    Ruta 1: Recibe el NFA en un diccionario/JSON y devuelve el DFA.
    """
    try:
        if not isinstance(carga, dict):
            raise ValueError("The request body must be a JSON object")

        _requerir_campo_payload(carga, "states")
        _requerir_campo_payload(carga, "alphabet")
        _requerir_campo_payload(carga, "initial")
        _requerir_campo_payload(carga, "accepting")
        _requerir_campo_payload(carga, "transitions")

        resultado = AutomataGateway.procesar_conversion(carga)
        return resultado
    except Exception as e:
        raise HTTPException(status_code=400, detail=str(e))

@router.post("/simulate")
def simular_dfa_endpoint(carga: dict):
    """
    Ruta 2: Recibe el DFA y la palabra a probar ('input_string').
    """
    try:
        if not isinstance(carga, dict):
            raise ValueError("The request body must be a JSON object")

        dfa_datos = carga.get("dfa")
        cadena = carga.get("input_string")

        if dfa_datos is None:
            raise ValueError("Missing required field: dfa")

        if cadena is None:
            raise ValueError("Missing required field: input_string")

        if not isinstance(dfa_datos, dict):
            raise ValueError("The 'dfa' field must be a JSON object")

        if not isinstance(cadena, str):
            raise ValueError("The 'input_string' field must be a string")

        resultado = AutomataGateway.procesar_simulacion(dfa_datos, cadena)
        return resultado
    except Exception as e:
        raise HTTPException(status_code=400, detail=str(e))