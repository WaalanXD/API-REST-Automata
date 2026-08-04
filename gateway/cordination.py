# gateway/coordinator.py

def process_conversion(nfa_data):
    # Aquí irá el bloque try/except y la llamada a tu algoritmo real de 'functions'.
    # Por ahora, devolvemos el ejemplo estático del documento para probar la API[cite: 1].
    return {
        "dfaStates": [
            "0137",
            "247",
            "68",
            "58",
            "8"
        ],
        "transitions": [
            # Aquí irán las transiciones generadas...
        ],
        "acceptingStates": [
            "247",
            "68",
            "58",
            "8"
        ]
    }

def process_simulation(simulation_data):
    # Aquí se llamará a la lógica de simulación[cite: 1].
    return {
        "path": ["0137", "247", "58"],
        "accepted": True
    }