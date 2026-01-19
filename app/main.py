from fastapi import FastAPI, Header, HTTPException
from app.models import CreateDraftRequest, RejectDraftRequest
from app.services.draft_service import create_draft, get_draft, update_draft
from app.services.approval_service import approve_draft, reject_draft
from app.services.publish_service import publish_draft


app = FastAPI()

@app.post("/drafts")
def create_metadata_draft(
    request: CreateDraftRequest,
    x_user: str = Header(default="system")
):
    draft = create_draft(
        project=request.project,
        dataset=request.dataset,
        table=request.table,
        user=x_user
    )
    return draft

@app.get("/drafts/{draft_id}")
def read_metadata_draft(draft_id: str):
    try:
        return get_draft(draft_id)
    except ValueError:
        raise HTTPException(status_code=404, detail="Draft not found")

@app.put("/drafts/{draft_id}")
def edit_metadata_draft(
    draft_id: str,
    metadata_json: dict,
    x_user: str = Header(default="system")
):
    try:
        update_draft(
            draft_id=draft_id,
            metadata_json=metadata_json,
            user=x_user
        )
        return {"status": "updated"}
    except ValueError:
        raise HTTPException(status_code=404, detail="Draft not found")
    except RuntimeError as e:
        raise HTTPException(status_code=400, detail=str(e))

@app.post("/drafts/{draft_id}/approve")
def approve(
    draft_id: str,
    x_user: str = Header(default="system")
):
    try:
        approve_draft(draft_id, x_user)
        return {"status": "approved"}
    except ValueError:
        raise HTTPException(status_code=404, detail="Draft not found")
    except RuntimeError as e:
        raise HTTPException(status_code=400, detail=str(e))


@app.post("/drafts/{draft_id}/reject")
def reject(
    draft_id: str,
    payload: RejectDraftRequest,
    x_user: str = Header(default="system")
):
    try:
        reject_draft(
            draft_id,
            x_user,
            payload.reason
        )
        return {"status": "rejected"}
    except ValueError:
        raise HTTPException(status_code=404, detail="Draft not found")
    except RuntimeError as e:
        raise HTTPException(status_code=400, detail=str(e))

@app.post("/drafts/{draft_id}/publish")
def publish(
    draft_id: str,
    x_user: str = Header(default="system")
):
    try:
        publish_draft(draft_id, x_user)
        return {"status": "published"}
    except ValueError:
        raise HTTPException(status_code=404, detail="Draft not found")
    except RuntimeError as e:
        raise HTTPException(status_code=400, detail=str(e))
