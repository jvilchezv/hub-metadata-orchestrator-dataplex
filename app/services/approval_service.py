from app.models import DraftStatus
from app.adapters.bq_draft_store import BigQueryDraftStore

draft_store = BigQueryDraftStore()


def approve_draft(draft_id: str, user: str):
    draft = draft_store.get_draft(draft_id)

    if not draft:
        raise ValueError("Draft not found")

    if draft["status"] != DraftStatus.DRAFT.value:
        raise RuntimeError(f"Draft in status {draft['status']} cannot be approved")

    draft_store.update_status(
        draft_id=draft_id, status=DraftStatus.APPROVED.value, user=user
    )


def reject_draft(draft_id: str, user: str, reason: str):
    draft = draft_store.get_draft(draft_id)

    if not draft:
        raise ValueError("Draft not found")

    if draft["status"] != DraftStatus.DRAFT.value:
        raise RuntimeError(f"Draft in status {draft['status']} cannot be rejected")

    draft_store.update_status(
        draft_id=draft_id,
        status=DraftStatus.REJECTED.value,
        user=user,
        rejection_reason=reason,
    )
