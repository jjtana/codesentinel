# Configuración del entorno de desarrollo

## Requisitos

- Python 3.12 (o superior)
- Git
- Editor recomendado: Visual Studio Code
  - Extensión: Python (Microsoft)
  - Extensión: SQLite Viewer (opcional, para ver la base de datos)

## Pasos de instalación

1. Clonar el repositorio:
   ```
   git clone <url-del-repositorio>
   cd codesentinel
   ```

2. Crear y activar un entorno virtual:
   ```
   cd backend
   python -m venv venv

   # Windows
   venv\Scripts\activate

   # macOS / Linux
   source venv/bin/activate
   ```

3. Instalar las dependencias:
   ```
   pip install -r requirements.txt
   ```

4. Crear el archivo de variables de entorno:
   ```
   cp .env.example .env
   ```
   Luego abrir `.env` y completar `AI_API_KEY` con tu llave de Gemini o Groq
   (ver sección "Proveedor de IA" más abajo).

5. Levantar el servidor de desarrollo:
   ```
   uvicorn app.main:app --reload
   ```

6. Verificar que funciona abriendo en el navegador:
   - API: http://localhost:8000
   - Documentación interactiva (Swagger): http://localhost:8000/docs

7. Abrir las pantallas del frontend directamente en el navegador
   (están en la carpeta `frontend/`, son archivos .html independientes
   mientras no se conectan todavía a la API).

## Proveedor de IA

El proyecto usa un proveedor de IA gratuito. Se puede alternar entre
dos opciones cambiando la variable `AI_PROVIDER` en `.env`:

| Proveedor | Variable | Dónde obtener la llave |
|---|---|---|
| Gemini (principal) | `AI_PROVIDER=gemini` | https://aistudio.google.com |
| Groq (respaldo)    | `AI_PROVIDER=groq`   | https://console.groq.com |

## Ejecutar las pruebas

```
cd backend
pytest tests/ -v
```

## Notas

- La base de datos de desarrollo es SQLite (`codesentinel.db`), se crea
  automáticamente al levantar el servidor. No se sube al repositorio
  (ver `.gitignore`).
- El archivo `.env` tampoco se sube al repositorio porque contiene llaves
  privadas; por eso existe `.env.example` como plantilla.
