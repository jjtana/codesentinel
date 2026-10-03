"""Prueba mínima: confirma que la API arranca y responde."""
import sys
import os

sys.path.insert(0, os.path.join(os.path.dirname(__file__), ".."))

from fastapi.testclient import TestClient
from app.main import app

client = TestClient(app)


def test_estado_api():
    respuesta = client.get("/")
    assert respuesta.status_code == 200
    assert respuesta.json()["proyecto"] == "CodeSentinel"
