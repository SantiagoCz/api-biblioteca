import json
from pathlib import Path

from app.modelos.libro import Libro, LibroEntrada

RUTA_ARCHIVO = Path(__file__).resolve().parent.parent / "datos" / "libros.json"

_libros: list[Libro] = []
_contador: int = 1

def cargar() -> None:
    global _libros, _contador
    try:
        datos = json.loads(RUTA_ARCHIVO.read_text(encoding="utf-8"))
        _libros = [Libro(**d) for d in datos]
    except (OSError, ValueError, TypeError):
        _libros = []
    _contador = max((libro.id for libro in _libros), default=0) + 1


def guardar() -> None:
    RUTA_ARCHIVO.parent.mkdir(exist_ok=True)
    contenido = [libro.model_dump() for libro in _libros]
    RUTA_ARCHIVO.write_text(
        json.dumps(contenido, ensure_ascii=False, indent=2),
        encoding="utf-8",
    )


def obtener_todos() -> list[Libro]:
    return list(_libros)


def crear(datos: LibroEntrada) -> Libro:
    global _contador
    libro = Libro(id=_contador, **datos.model_dump())
    _contador += 1
    _libros.append(libro)
    guardar()
    return libro