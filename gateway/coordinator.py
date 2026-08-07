# gateway/coordinator.py
from functions.automata_logic import nfa_a_dfa, simular_dfa

class AutomataGateway:
    @staticmethod
    def procesar_conversion(carga: dict) -> dict:
        """
        Llama a la lógica central para convertir NFA a DFA y maneja excepciones.
        """
        try:
            # Coordinar la ejecución (Responsabilidad 1)
            return nfa_a_dfa(carga)
        except Exception as e:
            # Manejar excepciones (Responsabilidad 2)
            return {"error": "Internal error while executing the conversion algorithm.", "detail": str(e)}

    @staticmethod
    def procesar_simulacion(dfa: dict, cadena: str) -> dict:
        """
        Llama a la lógica central para simular el AFD y maneja excepciones.
        """
        try:
            return simular_dfa(dfa, cadena)
        except Exception as e:
            return {"error": "Internal error while executing the simulation.", "detail": str(e)}