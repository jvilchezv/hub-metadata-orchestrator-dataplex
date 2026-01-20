from google.cloud import dataplex_v1
from google.api_core.client_options import ClientOptions
from typing import Optional
from google.protobuf import field_mask_pb2
import logging

logger = logging.getLogger(__name__)


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
        self.client = dataplex_v1.CatalogServiceClient(
            credentials=credentials, client_options=client_options
        )

    def publish_descriptions(self, entry_name: str, aspects: dict):
        entry = dataplex_v1.Entry(name=entry_name, aspects=aspects)
        mask = field_mask_pb2.FieldMask(paths=["aspects"])

        self.client.update_entry(entry=entry, update_mask=mask)
