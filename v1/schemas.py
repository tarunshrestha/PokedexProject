from pydantic import BaseModel, Field
from uuid import UUID, uuid4
from typing import Optional, List, TypeVar, Generic

from pydantic.v1.generics import GenericModel

from models import Pokemon

T = TypeVar('T')


class PokemonSchema(BaseModel):
    id: int
    name: str
    moves: List[str]
    images: Optional[List[str]]

    class Config:
        orm_mode = True


class RequestPokemon(BaseModel):
    parameter: PokemonSchema = Field(..., description="Pokemon details")


class Response(Generic[T], GenericModel):
    code: int
    status: str
    message: List[str]
    result: Optional[T]
