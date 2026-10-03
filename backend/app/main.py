"""
CodeSentinel - Punto de entrada de la API
Proyecto Final ITLA
"""
from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware

from app.api import auth, ingesta, analisis, ia, reportes
from app.core.config import settings

app = FastAPI(
    title="CodeSentinel API",
    description="Plataforma de Análisis de Código y Calidad de Software con IA",
    version="0.1.0",
)

# CORS abierto en desarrollo; restringir en producción
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_methods=["*"],
    allow_headers=["*"],
)

# Cada módulo del proyecto vive en su propio router.
app.include_router(auth.router, prefix="/api/auth", tags=["Autenticación"])
app.include_router(ingesta.router, prefix="/api/ingesta", tags=["Módulo 1 - Ingesta"])
app.include_router(analisis.router, prefix="/api/analisis", tags=["Módulo 2 - Análisis"])
app.include_router(ia.router, prefix="/api/ia", tags=["Módulo 3 - Motor de IA"])
app.include_router(reportes.router, prefix="/api/reportes", tags=["Módulo 4 - Reportes"])


@app.get("/", tags=["Estado"])
def estado():
    """Endpoint de salud: confirma que la API está viva."""
    return {
        "proyecto": "CodeSentinel",
        "estado": "en desarrollo",
        "version": app.version,
    }
