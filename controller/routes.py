# controller/routes.py
from fastapi import APIRouter, HTTPException
from gateway.coordinator import AutomataGateway

router = APIRouter()

@router.post("/convert")
def convertir_nfa(carga: dict):
    """
    Ruta 1: Recibe el NFA en un JSON, valida que traiga los datos básicos y devuelve el DFA.
    """
    # 1. Validates input (Responsabilidad estricta del Controlador)
    campos_requeridos = ["states", "alphabet", "initial", "accepting", "transitions"]
    if not all(campo in carga for campo in campos_requeridos):
        # Si falta algún campo, el controlador responde inmediatamente con un error 400.
        raise HTTPException(status_code=400, detail="Missing required NFA fields")
    
    # 2. Pasa la responsabilidad al Gateway (El Gateway ejecutará y atrapará los errores/excepciones)
    return AutomataGateway.procesar_conversion(carga)


@router.post("/simulate")
def simular_dfa_endpoint(carga: dict):
    """
    Ruta 2: Recibe el DFA y la palabra a probar ('input_string').
    """
    # 1. Validates input[cite: 1]
    if "dfa" not in carga or "input_string" not in carga:
        raise HTTPException(status_code=400, detail="Missing required fields: dfa or input_string")
        
    # 2. Pasa la responsabilidad al Gateway
    return AutomataGateway.procesar_simulacion(carga["dfa"], carga["input_string"])