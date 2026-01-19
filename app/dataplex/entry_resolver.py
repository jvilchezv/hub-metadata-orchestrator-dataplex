from app.config import DATAPLEX_LOCATION


def build_bq_entry_name(project: str, dataset: str, table: str) -> str:
    return (
        f"projects/{project}/locations/{DATAPLEX_LOCATION}"
        f"/entryGroups/@bigquery/entries/"
        f"bigquery.googleapis.com/projects/{project}"
        f"/datasets/{dataset}/tables/{table}"
    )
