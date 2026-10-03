"""
Módulo 1 - Ingesta.
Pendiente: clonar el repositorio recibido, recorrer sus archivos .py
y encolar el análisis (ver docs/ROADMAP.md, semanas 3-5).
"""
from fastapi import APIRouter

router = APIRouter()


@router.post("/repositorio")
def registrar_repositorio():
    """Recibirá la URL de un repositorio de GitHub/GitLab para analizarlo."""
    return {"modulo": "ingesta", "estado": "en construcción"}


@router.get("/proyectos")
def listar_proyectos():
    return {"modulo": "ingesta", "estado": "en construcción", "proyectos": []}
