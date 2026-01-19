from enum import Enum
from pydantic import BaseModel
from typing import Optional, Dict, Any
from datetime import datetime


class DraftStatus(str, Enum):
    DRAFT = "DRAFT"
    APPROVED = "APPROVED"
    REJECTED = "REJECTED"
    PUBLISHED = "PUBLISHED"


class CreateDraftRequest(BaseModel):
    project: str
    dataset: str
    table: str


class MetadataDraft(BaseModel):
    draft_id: str
    fqdn: str
    status: DraftStatus
    metadata_json: Dict[str, Any]
    created_at: datetime
    created_by: Optional[str]


class DecisionRequest(BaseModel):
    reason: Optional[str] = None


class RejectDraftRequest(BaseModel):
    reason: str
