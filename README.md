# Metadata Orchestrator

Service responsible for:
- Requesting metadata generation
- Managing metadata drafts
- Human approval / rejection workflow
- Publishing approved metadata to Dataplex

This service does NOT:
- Generate metadata using LLMs
- Profile BigQuery tables

| Acción UI | API                         |
| --------- | --------------------------- |
| Generate  | `POST /drafts`              |
| View      | `GET /drafts/{id}`          |
| Edit      | `PUT /drafts/{id}`          |
| Approve   | `POST /drafts/{id}/approve` |
| Reject    | `POST /drafts/{id}/reject`  |
| Publish   | `POST /drafts/{id}/publish` |

hub-metadata-generator-ai
hub-metadata-orchestrator-dataplex
