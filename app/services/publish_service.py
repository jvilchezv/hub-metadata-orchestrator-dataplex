from app.adapters.bq_draft_store import BigQueryDraftStore
from app.dataplex.entry_resolver import build_bq_entry_name
from app.dataplex.dataplex_mapper import map_metadata_to_descriptions_aspect
from app.dataplex.dataplex_publisher import DataplexPublisher
from app.models import DraftStatus


draft_store = BigQueryDraftStore()
publisher = DataplexPublisher()


def publish_draft(draft_id: str, user: str):
    draft = draft_store.get_draft(draft_id)

    if not draft:
        raise ValueError("Draft not found")

    if draft["status"] != DraftStatus.APPROVED.value:
        raise RuntimeError("Only APPROVED drafts can be published")

    entry_name = build_bq_entry_name(
        project=draft["project"], dataset=draft["dataset"], table=draft["table"]
    )

    aspects = map_metadata_to_descriptions_aspect(draft["metadata_json"])

    publisher.publish_descriptions(entry_name=entry_name, aspects=aspects)

    draft_store.update_status(
        draft_id=draft_id, status=DraftStatus.PUBLISHED.value, user=user
    )
