import requests
import google.auth.transport.requests
import google.oauth2.id_token
from app.config import METADATA_GENERATOR_URL, METADATA_GENERATOR_AUDIENCE


def generate_metadata(project: str, dataset: str, table: str) -> dict:
    url = f"{METADATA_GENERATOR_URL}/projects/{project}/datasets/{dataset}/tables/{table}"
    try:
        auth_req = google.auth.transport.requests.Request()
        id_token = google.oauth2.id_token.fetch_id_token(auth_req, METADATA_GENERATOR_AUDIENCE)
        headers = {
            "Authorization": f"Bearer {id_token}",
            "Content-Type": "application/json"
        }
        response = requests.post(
            url,
            headers=headers,
            timeout=120,
        )
        response.raise_for_status()

        return response.json()

    except requests.exceptions.RequestException as e:
        raise RuntimeError(f"Metadata generator call failed: {str(e)}")
