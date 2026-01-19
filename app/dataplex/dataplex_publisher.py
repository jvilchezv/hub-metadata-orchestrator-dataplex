from google.cloud import dataplex_v1


class DataplexPublisher:
    def __init__(self):
        self.client = dataplex_v1.DataplexServiceClient()

    def publish_descriptions(self, entry_name: str, aspects: dict):
        entry = dataplex_v1.Entry(name=entry_name, aspects=aspects)

        self.client.update_entry(entry=entry, update_mask="aspects")
