from typing import Optional

from pydantic import BaseModel


class StatusSchema(BaseModel):
    status: str

class TaskSchema(BaseModel):
    id: str
    name: str
    description: Optional[str] = None
    status: StatusSchema
