import requests
from app.config import METADATA_GENERATOR_URL


def generate_metadata(project: str, dataset: str, table: str) -> dict:
    try:
        response = requests.post(
            f"{METADATA_GENERATOR_URL}/projects/{project}/datasets/{dataset}/tables/{table}",
            timeout=120,
        )
        response.raise_for_status()
        return response.json()

    except requests.exceptions.RequestException as e:
        raise RuntimeError(f"Metadata generator call failed: {str(e)}")
