from google.cloud import dataplex_v1
from google.api_core.client_options import ClientOptions
from typing import Optional


class DataplexPublisher:
    def __init__(
        self,
        credentials: Optional[object] = None,
        client_options: Optional[ClientOptions] = None,
    ):
        """
        Initialize DataplexPublisher.

        Args:
            credentials: Optional credentials for authentication
            client_options: Optional client options (e.g., for regional endpoints)
        """
        self.client = dataplex_v1.DataplexServiceClient(
            credentials=credentials, client_options=client_options
        )

    def publish_descriptions(self, entry_name: str, aspects: dict):
        entry = dataplex_v1.Entry(name=entry_name, aspects=aspects)

        self.client.update_entry(entry=entry, update_mask="aspects")
