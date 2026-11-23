from fastapi import FastAPI, Request
from fastapi.responses import JSONResponse
from pydantic import ValidationError

from app.excepciones.errores import (
    EstadoLibroError,
    LibroDuplicadoError,
    LibroNoEncontradoError,
)


def registrar_manejadores(app: FastAPI) -> None:

    @app.exception_handler(LibroNoEncontradoError)
    def manejar_no_encontrado(request: Request, error: LibroNoEncontradoError):
        return JSONResponse(status_code=404, content={"detail": error.mensaje})

    @app.exception_handler(LibroDuplicadoError)
    def manejar_duplicado(request: Request, error: LibroDuplicadoError):
        return JSONResponse(status_code=409, content={"detail": error.mensaje})

    @app.exception_handler(ValidationError)
    def manejar_validacion(request: Request, error: ValidationError):
        detalle = error.errors(include_url=False, include_context=False)
        return JSONResponse(status_code=422, content={"detail": detalle})

    @app.exception_handler(EstadoLibroError)
    def manejar_estado(request: Request, error: EstadoLibroError):
        return JSONResponse(status_code=409, content={"detail": error.mensaje})