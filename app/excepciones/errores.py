class ErrorDeNegocio(Exception):
    """Base de los errores que la API devuelve al cliente con un mensaje."""

    def __init__(self, mensaje: str):
        super().__init__(mensaje)
        self.mensaje = mensaje


class LibroNoEncontradoError(ErrorDeNegocio):
    """No existe un libro con ese id (404)."""


class LibroDuplicadoError(ErrorDeNegocio):
    """Ya existe un libro con el mismo título y autor (409)."""