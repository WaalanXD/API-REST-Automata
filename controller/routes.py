from fastapi import APIRouter,HTTPException
from gateway.coordinator import AutomataGateway

router= APIRouter()

@router.post("/convert")
def convertir_nfa(carga:dict):
    campos_requeridos = ["states","alphabet","initial" ,"accepting","transitions"]
    if not all(campo in carga for campo in campos_requeridos):
        raise HTTPException(status_code= 400,detail="Missing required NFA fields")
    
    return AutomataGateway.procesar_conversion(carga)
@router.post("/simulate")
def simular_dfa_endpoint(carga: dict):
    if "dfa" not in carga or "input_string" not in carga:
        raise HTTPException(status_code= 400,detail ="Missing required fields: dfa or input_string")
        
    return AutomataGateway.procesar_simulacion(carga["dfa"],carga["input_string"])
