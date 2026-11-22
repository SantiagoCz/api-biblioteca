from fastapi import APIRouter

from app.modelos.libro import Libro, LibroEntrada
from app.servicios import libros as servicio_libros

router = APIRouter(prefix="/libros", tags=["libros"])

# CREATE
@router.post("", response_model=Libro, status_code=201)
def crear_libro(entrada: LibroEntrada):
    return servicio_libros.crear_libro(entrada)

# READ
@router.get("", response_model=list[Libro])
def listar_libros():
    return servicio_libros.listar_libros()

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

# DELETE
@router.delete("/{libro_id}", status_code=204)
def eliminar_libro(libro_id: int):
    servicio_libros.eliminar_libro(libro_id)