# gateway/coordinator.py

from functions.automata_logic import nfa_a_dfa, simular_dfa

class AutomataGateway:
    @staticmethod
    def procesar_conversion(carga: dict) -> dict:
        """
        Llama a la lógica central para convertir AFN a AFD.
        """
        # Aquí podrías agregar validaciones adicionales de la carga si lo deseas.
        return nfa_a_dfa(carga)

    @staticmethod
    def procesar_simulacion(dfa: dict, cadena: str) -> dict:
        """
        Llama a la lógica central para simular el AFD.
        """
        return simular_dfa(dfa, cadena)