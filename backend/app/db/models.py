"""
Modelos de datos iniciales. Se irán completando a medida que
se desarrolle cada módulo (ver docs/ROADMAP.md).
"""
from sqlalchemy import Column, Integer, String, DateTime, ForeignKey, Text
from sqlalchemy.sql import func

from app.db.database import Base


class Usuario(Base):
    __tablename__ = "usuarios"

    id = Column(Integer, primary_key=True, index=True)
    nombre = Column(String(120), nullable=False)
    correo = Column(String(120), unique=True, nullable=False)
    password_hash = Column(String(255), nullable=False)
    creado_en = Column(DateTime(timezone=True), server_default=func.now())


class Proyecto(Base):
    __tablename__ = "proyectos"

    id = Column(Integer, primary_key=True, index=True)
    usuario_id = Column(Integer, ForeignKey("usuarios.id"))
    nombre = Column(String(150), nullable=False)
    url_repositorio = Column(String(300), nullable=False)
    creado_en = Column(DateTime(timezone=True), server_default=func.now())


class Analisis(Base):
    __tablename__ = "analisis"

    id = Column(Integer, primary_key=True, index=True)
    proyecto_id = Column(Integer, ForeignKey("proyectos.id"))
    estado = Column(String(30), default="pendiente")  # pendiente | en_progreso | completo
    iniciado_en = Column(DateTime(timezone=True), server_default=func.now())


class Hallazgo(Base):
    __tablename__ = "hallazgos"

    id = Column(Integer, primary_key=True, index=True)
    analisis_id = Column(Integer, ForeignKey("analisis.id"))
    archivo = Column(String(300))
    linea = Column(Integer)
    severidad = Column(String(20))  # baja | media | alta | critica
    descripcion = Column(Text)
    explicacion_ia = Column(Text, nullable=True)
    sugerencia_ia = Column(Text, nullable=True)
    score_riesgo = Column(Integer, nullable=True)
