# gateway/coordinator.py

from functions.automata_logic import nfa_to_dfa, simulate_dfa

class AutomataGateway:
    @staticmethod
    def process_conversion(payload: dict) -> dict:
        """
        Llama a la lógica central para convertir AFN a AFD.
        """
        # Aquí podrías agregar validaciones adicionales del payload si lo deseas
        return nfa_to_dfa(payload)

    @staticmethod
    def process_simulation(dfa: dict, cadena: str) -> dict:
        """
        Llama a la lógica central para simular el AFD.
        """
        return simulate_dfa(dfa, cadena)