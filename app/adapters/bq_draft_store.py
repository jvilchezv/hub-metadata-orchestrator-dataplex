from google.cloud import bigquery
from datetime import datetime, timezone
from app.config import GCP_PROJECT_ID, DRAFT_DATASET, DRAFT_TABLE


class BigQueryDraftStore:
    def __init__(self):
        self.client = bigquery.Client(project=GCP_PROJECT_ID)
        self.table_id = f"{GCP_PROJECT_ID}.{DRAFT_DATASET}.{DRAFT_TABLE}"

    def insert_draft(self, draft: dict):
        job_config = bigquery.LoadJobConfig(
            source_format=bigquery.SourceFormat.NEWLINE_DELIMITED_JSON,
            write_disposition="WRITE_APPEND",
        )

        try:
            job = self.client.load_table_from_json(
                [draft], 
                self.table_id, 
                job_config=job_config
            )
            job.result()

        except Exception as e:
            print(f"Error detallado en la carga a BigQuery: {str(e)}")
            raise RuntimeError(f"Failed to insert draft: {str(e)}")


    def get_draft(self, draft_id: str) -> dict | None:
        query = f"""
        SELECT *
        FROM `{self.table_id}`
        WHERE draft_id = @draft_id
        LIMIT 1
        """

        job = self.client.query(
            query,
            job_config=bigquery.QueryJobConfig(
                query_parameters=[
                    bigquery.ScalarQueryParameter("draft_id", "STRING", draft_id)
                ]
            ),
        )

        rows = list(job.result())
        if not rows:
            return None

        return dict(rows[0])

    def update_draft(self, draft_id: str, metadata_json: dict, updated_by: str):
        query = f"""
        UPDATE `{self.table_id}`
        SET
          metadata_json = @metadata_json,
          updated_at = @updated_at,
          updated_by = @updated_by
        WHERE draft_id = @draft_id
        """

        job_config = bigquery.QueryJobConfig(
            query_parameters=[
                bigquery.ScalarQueryParameter("metadata_json", "JSON", metadata_json),
                bigquery.ScalarQueryParameter(
                    "updated_at", "TIMESTAMP", datetime.now(timezone.utc)
                ),
                bigquery.ScalarQueryParameter("updated_by", "STRING", updated_by),
                bigquery.ScalarQueryParameter("draft_id", "STRING", draft_id),
            ]
        )

        self.client.query(query, job_config=job_config).result()

    def update_status(
        self, draft_id: str, status: str, user: str, rejection_reason: str | None = None
    ):
        query = f"""
        UPDATE `{self.table_id}`
        SET
          status = @status,
          updated_at = @updated_at,
          updated_by = @user,
          approved_at = IF(@status = 'APPROVED', @updated_at, approved_at),
          approved_by = IF(@status = 'APPROVED', @user, approved_by),
          rejection_reason = @rejection_reason
        WHERE draft_id = @draft_id
        """

        job_config = bigquery.QueryJobConfig(
            query_parameters=[
                bigquery.ScalarQueryParameter("status", "STRING", status),
                bigquery.ScalarQueryParameter(
                    "updated_at", "TIMESTAMP", datetime.now(timezone.utc)
                ),
                bigquery.ScalarQueryParameter("user", "STRING", user),
                bigquery.ScalarQueryParameter(
                    "rejection_reason", "STRING", rejection_reason
                ),
                bigquery.ScalarQueryParameter("draft_id", "STRING", draft_id),
            ]
        )

        self.client.query(query, job_config=job_config).result()
