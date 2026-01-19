# Orquestador de Metadatos

Servicio especializado en la gestión integral del ciclo de vida de metadatos en Dataplex.

## Descripción

Este servicio es responsable de:

- 📤 Solicitar la generación de metadatos
- 📝 Administrar borradores de metadatos
- ✅ Gestionar flujos de aprobación y rechazo por usuarios
- 🚀 Publicar metadatos aprobados en Dataplex

### Fuera del alcance de este servicio:

- ❌ Generación de metadatos usando LLMs
- ❌ Perfilado (profiling) de tablas en BigQuery

## 🔌 Endpoints de API

| Acción en UI | Método HTTP | Endpoint                 | Descripción         |
| ------------- | ------------ | ------------------------ | -------------------- |
| Generar       | `POST`     | `/drafts`              | Crear nuevo borrador |
| Ver           | `GET`      | `/drafts/{id}`         | Obtener borrador     |
| Editar        | `PUT`      | `/drafts/{id}`         | Modificar borrador   |
| Aprobar       | `POST`     | `/drafts/{id}/approve` | Aprobar metadatos    |
| Rechazar      | `POST`     | `/drafts/{id}/reject`  | Rechazar metadatos   |
| Publicar      | `POST`     | `/drafts/{id}/publish` | Publicar en Dataplex |

## Servicios relacionados

- **[hub-metadata-generator-ai](https://github.com/...)** - Generador de metadatos con IA
- **[hub-metadata-orchestrator-dataplex](https://github.com/...)** - Este repositorio

## Instalación

```bash
pip install -r requirements.txt
```

## Uso

```bash
uvicorn app.main:app --reload
```

La aplicación estará disponible en `http://localhost:8000`

## Estructura del proyecto

```
app/
├── main.py                    # Punto de entrada de la aplicación
├── config.py                  # Configuración de la aplicación
├── models.py                  # Modelos de datos
├── adapters/                  # Adaptadores externos
│   ├── bq_draft_store.py     # Almacenamiento en BigQuery
│   └── metadata_api_client.py # Cliente de API de metadatos
├── dataplex/                  # Integración con Dataplex
│   ├── dataplex_mapper.py    # Mapeo de datos
│   ├── dataplex_publisher.py # Publicador de metadatos
│   └── entry_resolver.py     # Resolvedor de entradas
└── services/                  # Servicios de negocio
    ├── approval_service.py    # Servicio de aprobación
    ├── draft_service.py       # Servicio de borradores
    └── publish_service.py     # Servicio de publicación
```
