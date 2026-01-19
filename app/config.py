import os

METADATA_GENERATOR_URL = os.getenv(
    "METADATA_GENERATOR_URL",
    "https://metadata-api-zgs4exg6rq-uk.a.run.app"
)
# GCP_PROJECT_ID = os.getenv("GCP_PROJECT_ID", "my-gcp-project")
# DRAFT_DATASET = os.getenv("DRAFT_DATASET", "governance_metadata")
# DRAFT_TABLE = os.getenv("DRAFT_TABLE", "metadata_drafts")


# Proyecto de GOBIERNO (Aspect Types viven aquí)
DATAPLEX_GOV_PROJECT = os.getenv(
    "DATAPLEX_GOV_PROJECT",
    "rs-nprd-dlk-dd-trsv-ede4"
)

DATAPLEX_LOCATION = os.getenv(
    "DATAPLEX_LOCATION",
    "us"
)

# BigQuery drafts
GCP_PROJECT_ID = os.getenv("GCP_PROJECT_ID")
DRAFT_DATASET = os.getenv("DRAFT_DATASET", "governance_metadata")
DRAFT_TABLE = os.getenv("DRAFT_TABLE", "metadata_drafts")
