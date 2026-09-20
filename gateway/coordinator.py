from functions.automata_logic import nfa_a_dfa, simular_dfa, minimize_dfa

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
    @staticmethod
    def procesar_minimizacion(carga: dict) -> dict:
        try:
            n = carga.get("n")
            alphabet = carga.get("alphabet")
            final_states = carga.get("final_states")
            transitions = carga.get("transitions")
            
            equivalent_pairs = minimize_dfa(n, alphabet, final_states, transitions)
            
            # Formatear la salida adecuadamente
            formatted_pairs = [[p, q] for p, q in equivalent_pairs]
            
            return {
                "equivalent_states": formatted_pairs,
                "total_pairs": len(formatted_pairs)
            }
        except Exception as e:
            return {
                "error": "Internal error while executing the minimization algorithm.",
                "detail": str(e)
            }
