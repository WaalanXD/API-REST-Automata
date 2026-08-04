# app.py


from fastapi import FastAPI
from controller.routes import router

app = FastAPI(title="API REST Automata")

# Incluimos las rutas definidas en controller/routes.py
app.include_router(router)

# Tienes que importar el router que creamos
from controller.routes import router

# Y luego, debajo de donde creas tu app = FastAPI(), debes incluir el router:
app.include_router(router)