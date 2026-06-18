from pydantic import BaseModel
from typing import Optional

class ListSchema(BaseModel):
    id: str
    name: str
    content: Optional[str] = None