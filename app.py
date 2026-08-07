# app.py


from fastapi import FastAPI
from controller.routes import router

app = FastAPI(title="API REST Automata")

app.include_router(router)


