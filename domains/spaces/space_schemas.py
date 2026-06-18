from typing import Any, Dict

from pydantic import BaseModel


class SpaceSchema(BaseModel):
    """
    Strict validator for a Space response.
    """

    id: str
    name: str
    private: bool
    statuses: list
    multiple_assignees: bool
    features: Dict[str, Any]
    archived: bool
