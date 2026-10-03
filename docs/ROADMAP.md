# Roadmap técnico — CodeSentinel

Periodo: 23 de septiembre al 15 de diciembre de 2026 (12 semanas).

| Semana | Entregable técnico | Estado |
|---|---|---|
| 1–2 | Repositorio, estructura de carpetas, entorno configurado, modelos de base de datos, pantallas en blanco | ✅ Completado (esta entrega) |
| 3–5 | Módulo 1 (Ingesta): clonar repositorio, recorrer archivos .py, encolar análisis | ⬜ Pendiente |
| 3–5 | Módulo 2 (Análisis): integrar Bandit y radon, reglas propias con `ast`, guardar hallazgos | ⬜ Pendiente |
| 6–8 | Módulo 3 (Motor de IA): explicación y sugerencia de corrección por hallazgo, score de riesgo, trazabilidad de versión del modelo | ⬜ Pendiente |
| 9–10 | Módulo 4 (Reportes): dashboard con gráficos, exportación PDF/HTML, login funcional | ⬜ Pendiente |
| 11–12 | Pruebas con usuarios, documentación final, manual de usuario, ensayo de presentación | ⬜ Pendiente |

## Arquitectura técnica

- **Backend:** Python 3.12 + FastAPI, organizado en un router por módulo.
- **Base de datos:** SQLite en desarrollo (migrable a PostgreSQL o SQL Server).
- **Frontend:** HTML + CSS + JavaScript, con Tailwind y Chart.js cuando se conecten los datos.
- **Análisis estático:** Bandit (seguridad) y radon (complejidad), más reglas propias con el módulo `ast`.
- **IA:** proveedor gratuito (Gemini o Groq), intercambiable por configuración (`AI_PROVIDER` en `.env`).
- **CI:** GitHub Actions ejecuta las pruebas automáticas en cada Pull Request (`.github/workflows/ci.yml`).

## Convención de ramas (Git)

- `main`: versión estable, lista para presentar.
- `develop`: integración de los módulos en desarrollo.
- `feature/<modulo>`: una rama por módulo (ej. `feature/ingesta`, `feature/motor-ia`).

## Próximo hito

Semana 3: comenzar el Módulo 1 (Ingesta) — endpoint que reciba la URL de un
repositorio, lo clone y liste sus archivos Python.
