from typing import Optional

from pydantic import BaseModel


class ListSchema(BaseModel):
    id: str
    name: str
    content: Optional[str] = None
