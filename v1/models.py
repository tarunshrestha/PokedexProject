from sqlalchemy import Column, Integer, String, ARRAY
from database import Base


class Pokemon(Base):
    __tablename__ = 'pokemons'

    id = Column(Integer, primary_key=True)
    name = Column(String)
    moves = Column(String)
    type = Column(String)
    images = Column(String)
    detail_url = Column(String)

    def __str__(self):
        return self.name

