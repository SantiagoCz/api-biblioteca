from app.excepciones.errores import LibroDuplicadoError, LibroNoEncontradoError
from app.modelos.libro import Libro, LibroEntrada
from app.repositorios import libros as repositorio_libros

CAMPOS_EDITABLES = {"titulo", "autor", "anio", "disponible"}

# CREATE
def crear_libro(datos_nuevos: LibroEntrada) -> Libro:
    datos_normalizados = datos_nuevos.model_copy(update={
        "titulo": normalizar_texto(datos_nuevos.titulo),
        "autor": normalizar_texto(datos_nuevos.autor),
    })
    verificar_duplicado(datos_normalizados.titulo, datos_normalizados.autor)
    return repositorio_libros.crear(datos_normalizados)

# READ
def listar_libros() -> list[Libro]:
    return repositorio_libros.obtener_todos()

def obtener_libro(libro_id: int) -> Libro:
    libro = _buscar_libro(libro_id)
    if libro is None:
        raise LibroNoEncontradoError(f"No existe un libro con id {libro_id}.")
    return libro

# UPDATE
def actualizar_libro(libro_id: int, campos_recibidos: dict) -> Libro:
    libro_actual = obtener_libro(libro_id)
    cambios = filtrar_y_normalizar_cambios(campos_recibidos)
    libro_validado = combinar_y_validar_libro(libro_actual, cambios)
    verificar_duplicado(libro_validado.titulo, libro_validado.autor, excluir_id=libro_id)

    libro_actualizado = Libro(id=libro_id, **libro_validado.model_dump())
    return repositorio_libros.actualizar(libro_actualizado)

# DELETE
def eliminar_libro(libro_id: int) -> None:
    obtener_libro(libro_id)  # lanza 404 si no existe
    repositorio_libros.eliminar(libro_id)

# AUX METHODS
def _buscar_libro(libro_id: int) -> Libro | None:
    for libro in repositorio_libros.obtener_todos():
        if libro.id == libro_id:
            return libro
    return None

def normalizar_texto(texto: str) -> str:
    return " ".join(texto.split()).title()

def filtrar_y_normalizar_cambios(campos_recibidos: dict) -> dict:
    cambios_permitidos = {
        clave: valor
        for clave, valor in campos_recibidos.items()
        if clave in CAMPOS_EDITABLES
    }
    for campo in ("titulo", "autor"):
        if isinstance(cambios_permitidos.get(campo), str):
            cambios_permitidos[campo] = normalizar_texto(cambios_permitidos[campo])
    return cambios_permitidos

def combinar_y_validar_libro(libro_actual: Libro, cambios: dict) -> LibroEntrada:
    return LibroEntrada(**{**libro_actual.model_dump(), **cambios})

def verificar_duplicado(titulo: str, autor: str, excluir_id: int | None = None) -> None:
    # excluir_id evita que un libro se compare consigo mismo al editarlo
    for libro in repositorio_libros.obtener_todos():
        if libro.id == excluir_id:
            continue
        if libro.titulo.lower() == titulo.lower() and libro.autor.lower() == autor.lower():
            raise LibroDuplicadoError(f"Ya existe el libro '{titulo}' de {autor}.")