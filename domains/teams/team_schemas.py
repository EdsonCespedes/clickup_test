from typing import List
from pydantic import BaseModel


class TeamMember(BaseModel):
    id: int
    username: str
    email: str


class Team(BaseModel):
    id: str
    name: str
    members: List[dict]


class GetTeamsResponse(BaseModel):
    """
    Main schema used to validate the complete response from GET /team.
    """

    teams: List[Team]