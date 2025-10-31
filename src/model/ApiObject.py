from abc import ABC, abstractmethod


class ApiObject(ABC):
    """Interface that define a Object that was returned from the API"""

    @abstractmethod
    def toJSON(self, metadata=False, total_results=0) -> dict:
        """Returns a JSON Object of the Object"""
        pass

    @abstractmethod
    def __init__(self, row: list, base_url="") -> "ApiObject":
        """Create a object using a row from the query"""
        pass

    @abstractmethod
    def __init__(self, row: list, base_url="", id=0) -> "ApiObject":
        """Create a object using a row from the query"""
        pass
