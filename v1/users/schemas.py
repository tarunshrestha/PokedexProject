from pydantic import BaseModel
from uuid import UUID, uuid4
from typing import Optional, List
from .enums import Gender, Group


class User(BaseModel):
    id: Optional[UUID] = uuid4()
    username: str
    first_name: str
    last_name: Optional[str]
    gender: Gender
    group: List[Group]

    def __str__(self):
        return self.username
