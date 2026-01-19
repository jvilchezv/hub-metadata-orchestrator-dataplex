from datetime import datetime, timezone
import uuid

from app.models import DraftStatus
from app.adapters.metadata_api_client import generate_metadata
from app.adapters.bq_draft_store import BigQueryDraftStore


draft_store = BigQueryDraftStore()


def create_draft(project: str, dataset: str, table: str, user: str):
    metadata = generate_metadata(project, dataset, table)

    draft = {
        "draft_id": str(uuid.uuid4()),
        "fqdn": f"{project}.{dataset}.{table}",
        "status": DraftStatus.DRAFT.value,
        "metadata_json": metadata,
        "created_at": datetime.now(timezone.utc).strftime("%Y-%m-%d %H:%M:%S %Z"),
        "created_by": user,
        "updated_at": None,
        "updated_by": None,
        "decision_reason": None,
    }

    draft_store.insert_draft(draft)
    return draft


def get_draft(draft_id: str) -> dict:
    draft = draft_store.get_draft(draft_id)

    if not draft:
        raise ValueError("Draft not found")

    return draft


def update_draft(draft_id: str, metadata_json: dict, user: str):
    draft = draft_store.get_draft(draft_id)

    if not draft:
        raise ValueError("Draft not found")

    if draft["status"] != DraftStatus.DRAFT.value:
        raise RuntimeError(f"Cannot edit draft in status {draft['status']}")

    # 🔒 Aquí deberías reutilizar tu metadata_schema validator
    # validate_metadata_schema(metadata_json)

    draft_store.update_draft(
        draft_id=draft_id, metadata_json=metadata_json, updated_by=user
    )
