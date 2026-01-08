"""
Moduele written by Carlos Chacón.

Define the ButtersPunishments data model used to represent Butters' punishments
in the API responses. Each ButtersPunishments instance contains information about a specific
punishment including its ID, episode number, and reason for punishment.
"""

from pydantic import BaseModel

from src.model.ApiObject import ApiObject
from src.model.ORM.butters_punishments_db import ButtersPunishmentsDB


class ButtersPunishments(BaseModel, ApiObject):
    """
    Represents a Butters' punishment entry.

    Inherits from:
        BaseModel: Pydantic model for data validation
        ApiObject: Base interface for API response objects

    Attributes:
        id (int): Unique identifier for the punishment
        episode (int): Episode number where the punishment occurred
        reason_of_punishment (str): Reason for the punishment

    """

    id: int
    episode: str
    reason_of_punishment: str
    def toJSON(self, metadata: bool = False, total_results: int = 0) -> dict:
        """
        Convert the ButtersPunishments object to a JSON-compatible dictionary.

        Args:
            metadata (bool): Whether to include metadata in the response
            total_results (int): Total number of punishments in database

        Returns:
            dict: JSON-compatible dictionary with punishment data

        """
        if not metadata:
            return self.model_dump()
        else:
            result = dict()
            result["butters_punishment"] = self.model_dump()
            result["metadata"] = {
                "total_results": total_results
            }
            result["metadata"] = {
                "total_results": total_results
            }
            return result

    def __init__(self, db_object: ButtersPunishmentsDB, base_url: str = ""
                ) -> "ButtersPunishments":
            """
            Initialize ButtersPunishments from a ButtersPunishmentsDB object.

            Args:
                db_object (ButtersPunishmentsDB): Database object to initialize from
                base_url (str): Base URL for constructing episode link
            Returns:
                ButtersPunishments: Initialized ButtersPunishments instance

            """
            data = {
                "id": db_object.id,
                "episode": base_url + f"api/episodes/{db_object.episode}",
                "reason_of_punishment": db_object.reason_of_punishment,
            }
            super().__init__(**data)
