# NFA to DFA REST API

## Overview

This project is a REST web server that converts a non-deterministic finite automaton (NFA) into an equivalent deterministic finite automaton (DFA) using the subset construction algorithm.

The application also includes a DFA simulation endpoint that evaluates an input string and returns the traversal path plus the final acceptance result.

## Environment

- Operating system: Microsoft Windows NT 10.0.26200.0
- Shell: PowerShell 5.1.26100.8875
- Programming language: Python 3.14.4
- Main framework: FastAPI 0.141.1
- ASGI server: Uvicorn 0.52.1

## Project structure

- `app.py`: FastAPI application entry point
- `controller/routes.py`: HTTP routes
- `gateway/coordinator.py`: execution coordinator
- `functions/automata_logic.py`: NFA to DFA conversion and DFA simulation logic
- `pruebas.http`: sample requests for testing the API

## How to Run

1. Open a terminal in the project root.
2. Activate on windows the virtual environment:

	 ```powershell
	 .venv\Scripts\activate
	 ```

3. Start the server:

     ```powershell
   #Install the dependencies: pip install fastapi uvicorn
   
     uvicorn app:app --reload
     ```

4. Open the interactive API documentation at:

	 - `http://127.0.0.1:8000/docs`

## Endpoints

### POST /convert

Receives an NFA definition and returns the equivalent DFA.

Example request body:

```json
{
	"states": [0, 1, 2, 3, 4, 5, 6, 7, 8],
	"alphabet": ["a", "b"],
	"initial": [0],
	"accepting": [8],
	"transitions": [
		{ "from": 0, "symbol": "a", "to": 1 },
		{ "from": 1, "symbol": "b", "to": 2 }
	]
}
```

Example response shape:

```json
{
    "dfaStates": [
        "0",
        "1",
        "2"
    ],
    "transitions": [
        { "from": "0", "symbol": "a", "to": "1" },
        { "from": "1", "symbol": "b", "to": "2" }
    ],
    "acceptingStates": []
}
```

### POST /simulate

Receives a DFA and an input string, then returns the path followed by the automaton and whether the string was accepted.

Example request body:

```json
{
	"dfa": {
		"dfaStates": ["0", "0137", "247"],
		"transitions": [
			{ "from": "0", "symbol": "a", "to": "0137" },
			{ "from": "0137", "symbol": "b", "to": "247" }
		],
		"acceptingStates": ["247"]
	},
	"input_string": "ab"
}
```

Example response shape:

```json
{
    "path": [
        "0",
        "0137",
        "247"
    ],
    "accepted": true
}
```

## Algorithm Summary

The conversion uses the subset construction method:

1. Start with the initial NFA state as the first DFA state.
2. For each DFA state and each symbol in the alphabet, compute the union of all reachable NFA states.
3. Create a new DFA state for each new subset of NFA states.
4. Mark a DFA state as accepting if its subset contains at least one accepting NFA state.
5. Represent each DFA state as a sorted string of the NFA states that compose the subset.

The simulator reads the input string symbol by symbol, follows the DFA transitions, and returns the visited path and the final acceptance result.

## Notes

- The API is focused on explicit transitions and does not implement epsilon-closure handling.
- Sample requests are available in `pruebas.http`.
