import logging

from fastapi import FastAPI

from app.controladores import inicio, libros
from app.excepciones.manejadores import registrar_manejadores
from app.repositorios import libros as repo_libros

logging.basicConfig(level=logging.INFO)

app = FastAPI()

repo_libros.cargar()
registrar_manejadores(app)

app.include_router(inicio.router)
app.include_router(libros.router)