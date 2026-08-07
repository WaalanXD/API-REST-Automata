def nfa_a_dfa(datos_nfa: dict) -> dict:
    estados=datos_nfa["states"]
    alfabeto=datos_nfa["alphabet"]
    inicial= datos_nfa["initial"]
    aceptacion=datos_nfa["accepting"]
    transiciones=datos_nfa["transitions"]

    estado_inicial_lista=[inicial]
    estado_inicial_nombre= str(inicial)

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
