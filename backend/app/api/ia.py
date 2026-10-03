"""
Módulo 3 - Motor de IA.
Pendiente: enviar cada hallazgo relevante a un LLM (Gemini/Groq) para
explicación, sugerencia de corrección y cálculo de score de riesgo
(ver docs/ROADMAP.md, semanas 6-8).
"""
from fastapi import APIRouter

router = APIRouter()


@router.post("/hallazgos/{hallazgo_id}/explicar")
def explicar_hallazgo(hallazgo_id: int):
    return {"modulo": "ia", "estado": "en construcción", "hallazgo_id": hallazgo_id}
