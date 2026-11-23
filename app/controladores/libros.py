from fastapi import APIRouter, Query

from app.modelos.libro import Libro, LibroEntrada
from app.servicios import libros as servicio_libros

router = APIRouter(prefix="/libros", tags=["libros"])

# CREATE
@router.post("", response_model=Libro, status_code=201)
def crear_libro(entrada: LibroEntrada):
    return servicio_libros.crear_libro(entrada)

# READ
@router.get("", response_model=list[Libro])
def listar_libros(
    autor: str | None = None,
    disponible: bool | None = None,
    desde: int = Query(default=0, ge=0),
    limite: int = Query(default=100, ge=0),
):
    return servicio_libros.listar_libros(autor, disponible, desde, limite)

@router.get("/buscar", response_model=list[Libro])
def buscar_libros(texto: str):
    return servicio_libros.buscar_libros(texto)

@router.get("/estadisticas", response_model=dict[str, int])
def obtener_estadisticas():
    return servicio_libros.obtener_estadisticas()

@router.get("/{libro_id}", response_model=Libro)
def obtener_libro(libro_id: int):
    return servicio_libros.obtener_libro(libro_id)

# UPDATE
@router.put("/{libro_id}", response_model=Libro)
def actualizar_libro(libro_id: int, entrada: LibroEntrada):
    return servicio_libros.actualizar_libro(libro_id, entrada.model_dump())

@router.patch("/{libro_id}", response_model=Libro)
def actualizar_campo(libro_id: int, campos: dict):
    return servicio_libros.actualizar_libro(libro_id, campos)

@router.post("/{libro_id}/prestar", response_model=Libro)
def prestar_libro(libro_id: int):
    return servicio_libros.prestar_libro(libro_id)

@router.post("/{libro_id}/devolver", response_model=Libro)
def devolver_libro(libro_id: int):
    return servicio_libros.devolver_libro(libro_id)

# DELETE
@router.delete("/{libro_id}", status_code=204)
def eliminar_libro(libro_id: int):
    servicio_libros.eliminar_libro(libro_id)