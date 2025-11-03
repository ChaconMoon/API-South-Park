"""
Module written by Carlos Chacón.

This module defines the base ApiObject
interface that all API response models must implement.
It ensures consistent JSON serialization and object initialization across all models.
"""

from abc import ABC, abstractmethod


class ApiObject(ABC):
    """
    Abstract base class for all API response objects.

    This interface defines the common methods that all API response objects
    must implement to ensure consistent behavior across the API.

    All model classes that represent API responses should inherit from this class
    and implement its abstract methods.
    """

    @abstractmethod
    def toJSON(self, metadata: bool = False, total_results: int = 0) -> dict:
        """
        Convert the object to a JSON-compatible dictionary.

        Args:
            metadata (bool): Whether to include metadata in the response
            total_results (int): Total number of objects in database

        Returns:
            dict: JSON-compatible dictionary representation of the object

        """
        pass

    @abstractmethod
    def __init__(self, row: list, base_url: str = "") -> "ApiObject":
        """
        Initialize an object instance from database row data.

        Args:
            row (list): Database row containing object data
            base_url (str): Base URL for asset paths

        Returns:
            ApiObject: New object instance

        """
        pass
