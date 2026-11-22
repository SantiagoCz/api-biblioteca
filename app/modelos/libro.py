from pydantic import BaseModel, Field

class LibroEntrada(BaseModel):
    titulo: str = Field(min_length=3, max_length=100)
    autor: str = Field(min_length=3, max_length=60, pattern=r"^[A-Za-zÁÉÍÓÚáéíóúÑñÜü][A-Za-zÁÉÍÓÚáéíóúÑñÜü .'\-]*$")
    anio: int = Field(ge=1000, le=2026)
    disponible: bool = True

class Libro(LibroEntrada):
    id: int