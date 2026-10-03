"""
Autenticación de usuarios.
Pendiente: login con correo/contraseña, generación de JWT, OAuth con GitHub.
"""
from fastapi import APIRouter

router = APIRouter()


@router.post("/login")
def login():
    return {"modulo": "auth", "estado": "en construcción"}


@router.post("/registro")
def registro():
    return {"modulo": "auth", "estado": "en construcción"}
