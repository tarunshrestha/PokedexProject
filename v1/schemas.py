from pydantic import BaseModel
from uuid import UUID, uuid4
from typing import Optional, List


class Pokemon(BaseModel):
    added_by: List[User]
    id: int
    name: str
    moves: List[str]
    images: Optional[List[str]]

    def __str__(self):
        return self.username
