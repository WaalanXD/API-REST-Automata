from functions.automata_logic import nfa_a_dfa, simular_dfa

class AutomataGateway:
    @staticmethod
    def procesar_conversion(carga: dict)->dict:
        try:
            return nfa_a_dfa(carga)
        except Exception as e:
            return {"error": "Internal error while executing the conversion algorithm.","detail": str(e)}
    @staticmethod
    def procesar_simulacion(dfa: dict, cadena: str)->dict:
        try:
            return simular_dfa(dfa,cadena)
        except Exception as e:
            return {"error": "Internal error while executing the simulation.","detail": str(e)}
