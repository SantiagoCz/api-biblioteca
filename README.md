# API de la Biblioteca

API REST con FastAPI para gestionar libros de una biblioteca. Los datos se guardan en un archivo JSON y sobreviven al reinicio.

## Instalación

```bash
python -m venv .venv
source .venv/bin/activate
pip install -r requirements.txt
```

## Ejecución

```bash
uvicorn main:app --reload
```

Después abrí `http://127.0.0.1:8000/docs` para probar los endpoints.

## Decisiones

- El autor solo admite letras, espacios, puntos, apóstrofes y guiones, y tiene que empezar con una letra.
- Los textos de título y autor se normalizan al guardar: "bOrGEs" queda "Borges".
- El borrado es físico.
