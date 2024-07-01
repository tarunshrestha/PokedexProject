from sqlalchemy.orm import Session
from models import Pokemon
from schemas import PokemonSchema


def get_pokemons(db: Session, skip: int = 0, limit: int = 100):
    return db.query(Pokemon).offset(skip).limit(limit).all()


def get_pokemon_by_id(db: Session, pokemon_id: int):
    return db.query(Pokemon).filter(Pokemon.id == pokemon_id).first()


def create_pokemon(db: Session, pokemon: PokemonSchema):
    db.add(pokemon)
    db.commit()
    db.refresh(pokemon)
    return pokemon


def remove_pokemon(db: Session, pokemon_id: int):
    db.query(Pokemon).filter(Pokemon.id == pokemon_id).delete()
    db.commit()
