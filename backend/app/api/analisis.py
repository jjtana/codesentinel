"""
Módulo 2 - Análisis estático.
Pendiente: ejecutar Bandit (seguridad) y radon (complejidad), más reglas
propias con el módulo ast, y guardar los hallazgos (ver docs/ROADMAP.md).
"""
from fastapi import APIRouter

router = APIRouter()


@router.post("/{proyecto_id}/ejecutar")
def ejecutar_analisis(proyecto_id: int):
    return {"modulo": "analisis", "estado": "en construcción", "proyecto_id": proyecto_id}


@router.get("/{proyecto_id}/hallazgos")
def listar_hallazgos(proyecto_id: int):
    return {"modulo": "analisis", "estado": "en construcción", "hallazgos": []}
