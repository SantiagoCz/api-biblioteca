from fastapi import APIRouter

router = APIRouter()

@router.get("/")
def raiz():
    return {"mensaje": "API de la biblioteca"}