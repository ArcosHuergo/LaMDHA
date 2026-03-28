from fastapi import FastAPI
from controller import Router

app = FastAPI()

app.include_router(Router.api_router, prefix="/prueba")