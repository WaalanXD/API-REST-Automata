# gateway/coordinator.py
from functions.automata_logic import nfa_a_dfa, simular_dfa

class AutomataGateway:
    @staticmethod
    def procesar_conversion(carga: dict) -> dict:
        """
        Llama a la lógica central para convertir AFN a AFD y maneja excepciones.
        """
        try:
            # Coordinar la ejecución (Responsabilidad 1)
            return nfa_a_dfa(carga)
        except Exception as e:
            # Manejar excepciones (Responsabilidad 2)
            return {"error": "Error interno al ejecutar el algoritmo de conversión.", "detalle": str(e)}

    @staticmethod
    def procesar_simulacion(dfa: dict, cadena: str) -> dict:
        """
        Llama a la lógica central para simular el AFD y maneja excepciones.
        """
        try:
            return simular_dfa(dfa, cadena)
        except Exception as e:
            return {"error": "Error interno al ejecutar la simulación.", "detalle": str(e)}