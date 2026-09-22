def nfa_a_dfa(datos_nfa: dict) -> dict:
    estados=datos_nfa["states"]
    alfabeto=datos_nfa["alphabet"]
    inicial= datos_nfa["initial"]
    aceptacion=datos_nfa["accepting"]
    transiciones=datos_nfa["transitions"]

    iniciales = datos_nfa["initial"] 
    estado_inicial_lista = sorted(list(set(iniciales))) 
    estado_inicial_nombre = "".join(map(str, estado_inicial_lista))
    
    estados_dfa=[estado_inicial_nombre]
    transiciones_dfa=[]
    aceptacion_dfa=[]

    por_procesar=[estado_inicial_lista]
    procesados=[]

    while len(por_procesar)>0:
        grupo_actual=por_procesar.pop(0)
        procesados.append(grupo_actual)

        nombre_actual= "".join(map(str, sorted(grupo_actual)))

        es_final=False
        for estado in grupo_actual:
            if estado in aceptacion:
                es_final=True
                break

        if es_final and nombre_actual not in aceptacion_dfa:
            aceptacion_dfa.append(nombre_actual)

        for letra in alfabeto:
            nuevo_grupo=[]
            for estado in grupo_actual:
                for transicion in transiciones:
                    if transicion["from"]==estado and transicion["symbol"]==letra:
                        if transicion["to"] not in nuevo_grupo:
                            nuevo_grupo.append(transicion["to"])

            if len(nuevo_grupo)>0:
                nuevo_grupo.sort()
                nombre_nuevo= "".join(map(str, nuevo_grupo))

                transicion_dfa= {
                    "from": nombre_actual,
                    "symbol": letra,
                    "to": nombre_nuevo
                }

                if transicion_dfa not in transiciones_dfa:
                    transiciones_dfa.append(transicion_dfa)

                if nuevo_grupo not in procesados and nuevo_grupo not in por_procesar:
                    por_procesar.append(nuevo_grupo)
                    if nombre_nuevo not in estados_dfa:
                        estados_dfa.append(nombre_nuevo)

    return {
        "dfaStates": estados_dfa,
        "transitions": transiciones_dfa,
        "acceptingStates": aceptacion_dfa
    }

def simular_dfa(datos_dfa: dict, cadena_entrada: str)->dict:
    estados_dfa=datos_dfa["dfaStates"]
    transiciones=datos_dfa["transitions"]
    estados_aceptacion=datos_dfa["acceptingStates"]

    estado_actual=estados_dfa[0]
    camino=[estado_actual]

    for letra in cadena_entrada:
        se_movio=False
        for transicion in transiciones:
            if transicion["from"]==estado_actual and transicion["symbol"]==letra:
                estado_actual=transicion["to"]
                camino.append(estado_actual)
                se_movio=True
                break

        if not se_movio:
            return {
                "path": camino,
                "accepted": False
            }

    es_aceptada=estado_actual in estados_aceptacion

    return {
        "path": camino,
        "accepted": es_aceptada
    }

def minimize_dfa(n, alphabet, final_states, transitions):
    """
    Minimiza un DFA según el algoritmo de Kozen (Clases 13 y 14).
    :param n: int, número de estados (0 hasta n-1)
    :param alphabet: list de str, símbolos del alfabeto
    :param final_states: list de int, estados de aceptación
    :param transitions: dict o list de listas, tabla de transiciones donde 
                        transitions[q][a] da el estado al leer el símbolo a.
    :return: list de tuplas con los pares de estados equivalentes en orden lexicográfico.
    """
    final_set = set(final_states)
    
    # 1. Inicializar la tabla triangular para pares (p, q) con p < q
    # Marcamos True si son distinguibles, False si inicialmente se asumen equivalentes
    marked = [[False for _ in range(n)] for _ in range(n)]
    
    # Paso base: Un estado final y uno no final son distinguibles
    for p in range(n):
        for q in range(p + 1, n):
            if (p in final_set) != (q in final_set):
                marked[p][q] = True

    # 2. Iterar hasta que no haya cambios (marcar pares distinguibles)
    changed = True
    while changed:
        changed = False
        for p in range(n):
            for q in range(p + 1, n):
                if not marked[p][q]:
                    # Verificar si al leer cualquier símbolo del alfabeto llegan a estados distinguibles
                    for symbol_idx in range(len(alphabet)):
                        next_p = transitions[p][symbol_idx]
                        next_q = transitions[q][symbol_idx]
                        
                        # Ordenar los índices para acceder a la matriz triangular superior (row < col)
                        r, s = min(next_p, next_q), max(next_p, next_q)
                        if r != s and marked[r][s]:
                            marked[p][q] = True
                            changed = True
                            break

    # 3. Recolectar los pares que NO están marcados (es decir, son equivalentes)
    equivalent_pairs = []
    for p in range(n):
        for q in range(p + 1, n):
            if not marked[p][q]:
                equivalent_pairs.append((p, q))
                
    # Ordenar lexicográficamente (por defecto las tuplas se ordenan así)
    equivalent_pairs.sort()
    
    return equivalent_pairs
