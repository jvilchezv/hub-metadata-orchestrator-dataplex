from app.config import DATAPLEX_GOV_PROJECT, DATAPLEX_LOCATION


def map_metadata_to_descriptions_aspect(metadata_json: dict) -> dict:
    return {
        f"{DATAPLEX_GOV_PROJECT}.{DATAPLEX_LOCATION}.descriptions": {
            "data": {
                "description": metadata_json["table"]["description"],
                "fields": [
                    {
                        "name": col["name"],
                        "description": col["description"],
                        "fields": [],
                    }
                    for col in metadata_json.get("columns", [])
                ],
                "userManaged": True,
            }
        }
    }
