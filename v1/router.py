from fastapi import APIRouter, HTTPException, Path, Depends
from database import SessionLocal
from sqlalchemy.orm import Session
from schemas import PokemonSchema, RequestPokemon, Response
import crud

router = APIRouter()


def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()


@router.post('/create')
async def create_pokemon(request: RequestPokemon, db: Session = Depends(get_db)):
    crud.create_pokemon(db, request.parameters)
    return {'code': 200, 'message': 'Pokemon created', 'status': 'Ok'}


@router.get('/')
async def get_pokemons(db: Session = Depends(get_db)):
    pokemons = crud.get_pokemons(db, 0, 100)
    return {'code': 200, 'pokemons': pokemons}


@router.get('/{id}')
async def get_by_id(id: int, db: Session = Depends(get_db)):
    pokemon = crud.get_pokemon_by_id(db, id)
    return {'code': 200, 'pokemon': pokemon}


@router.delete('/{id}')
def delete_by_id(id: int, db: Session = Depends(get_db)):
    crud.remove_pokemon(db, id)
    return {'code': 200, 'message': 'Pokemon deleted'}