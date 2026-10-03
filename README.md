# CodeSentinel

Plataforma de Análisis de Código y Calidad de Software con Inteligencia Artificial.
Proyecto Final — ITLA.

## Estructura del proyecto

```
codesentinel/
├── backend/
│   ├── app/
│   │   ├── main.py            # Punto de entrada de la API (FastAPI)
│   │   ├── api/                # Un router por módulo
│   │   │   ├── auth.py
│   │   │   ├── ingesta.py       # Módulo 1
│   │   │   ├── analisis.py      # Módulo 2
│   │   │   ├── ia.py            # Módulo 3
│   │   │   └── reportes.py      # Módulo 4
│   │   ├── core/
│   │   │   └── config.py        # Configuración y variables de entorno
│   │   └── db/
│   │       ├── database.py      # Conexión a la base de datos
│   │       └── models.py        # Modelos: Usuario, Proyecto, Analisis, Hallazgo
│   ├── tests/
│   │   └── test_estado.py
│   └── requirements.txt
├── frontend/
│   ├── login.html
│   ├── dashboard.html
│   ├── proyectos.html
│   ├── reporte.html
│   └── static/
│       ├── css/style.css
│       └── js/
├── docs/
│   ├── ROADMAP.md
│   └── ENTORNO.md
├── .github/workflows/ci.yml
├── .env.example
└── .gitignore
```

## Cómo correr el proyecto

Ver `docs/ENTORNO.md` para la guía completa de instalación.

## Roadmap técnico

Ver `docs/ROADMAP.md`.
