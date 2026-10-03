"""
Módulo 4 - Reportes y dashboard.
Pendiente: métricas agregadas para el dashboard y exportación a
PDF/HTML (ver docs/ROADMAP.md, semanas 9-10).
"""
from fastapi import APIRouter

router = APIRouter()


@router.get("/{proyecto_id}/resumen")
def resumen_proyecto(proyecto_id: int):
    return {"modulo": "reportes", "estado": "en construcción", "proyecto_id": proyecto_id}


@router.get("/{proyecto_id}/exportar")
def exportar_reporte(proyecto_id: int):
    return {"modulo": "reportes", "estado": "en construcción"}
