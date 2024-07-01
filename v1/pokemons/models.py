from sqlalchemy import Column, Integer, String, Boolean, DateTime, ForeignKey, UniqueConstraint, URL
from v1.database import Base
from v1.users.models import User
from sqlalchemy.orm import relationship


class Pokemon(Base):
    __tablename__ = 'pokemons'

    id = Column(Integer, primary_key=True)
    name = Column(String)
    details = Column(String)
    added_by: Column(Integer, ForeignKey('users.id'))

    user = relationship("User", back_populates="pokemons")
