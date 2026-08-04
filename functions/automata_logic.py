# functions/automata_logic.py

def nfa_to_dfa(nfa_data: dict) -> dict:
    """
    Convierte un AFN a AFD juntando los estados en cadenas de texto (ej: '0137').
    """
    states = nfa_data["states"]
    alphabet = nfa_data["alphabet"]
    initial = nfa_data["initial"]
    accepting = nfa_data["accepting"]
    transitions = nfa_data["transitions"]

    estado_inicial_lista = [initial]
    estado_inicial_nombre = str(initial)

    dfa_states = [estado_inicial_nombre]
    dfa_transitions = []
    dfa_accepting = []

    por_procesar = [estado_inicial_lista]
    procesados = []

    while len(por_procesar) > 0:
        grupo_actual = por_procesar.pop(0)
        procesados.append(grupo_actual)

        nombre_actual = "".join(map(str, sorted(grupo_actual)))

        es_final = False
        for estado in grupo_actual:
            if estado in accepting:
                es_final = True
                break

        if es_final and nombre_actual not in dfa_accepting:
            dfa_accepting.append(nombre_actual)

        for letra in alphabet:
            nuevo_grupo = []
            for estado in grupo_actual:
                for t in transitions:
                    if t["from"] == estado and t["symbol"] == letra:
                        if t["to"] not in nuevo_grupo:
                            nuevo_grupo.append(t["to"])

            if len(nuevo_grupo) > 0:
                nuevo_grupo.sort()
                nombre_nuevo = "".join(map(str, nuevo_grupo))

                transicion_afd = {
                    "from": nombre_actual,
                    "symbol": letra,
                    "to": nombre_nuevo
                }

                if transicion_afd not in dfa_transitions:
                    dfa_transitions.append(transicion_afd)

                if nuevo_grupo not in procesados and nuevo_grupo not in por_procesar:
                    por_procesar.append(nuevo_grupo)
                    if nombre_nuevo not in dfa_states:
                        dfa_states.append(nombre_nuevo)

    return {
        "dfaStates": dfa_states,
        "transitions": dfa_transitions,
        "acceptingStates": dfa_accepting
    }

def simulate_dfa(dfa_data: dict, input_string: str) -> dict:
    """
    Recorre la palabra letra por letra sobre el AFD ya generado.
    """
    estados_dfa = dfa_data["dfaStates"]
    transiciones = dfa_data["transitions"]
    estados_aceptacion = dfa_data["acceptingStates"]

    estado_actual = estados_dfa[0]
    camino = [estado_actual]

    for letra in input_string:
        se_movio = False
        for t in transiciones:
            if t["from"] == estado_actual and t["symbol"] == letra:
                estado_actual = t["to"]
                camino.append(estado_actual)
                se_movio = True
                break

        if not se_movio:
            return {
                "path": camino,
                "accepted": False
            }

    es_aceptada = estado_actual in estados_aceptacion

    return {
        "path": camino,
        "accepted": es_aceptada
    }