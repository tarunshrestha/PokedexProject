import uuid
from typing import List
from sqlalchemy.orm import Session
from fastapi import FastAPI, Depends
from database import engine
from . import models
from database import SessionLocal, engine

app = FastAPI()

models.Base.metadata.create_all(bind=engine)

def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()


@app.get("/users/", response_model=List[User])
async def read_users(db: Session = Depends(get_db)):
    users = db.query(User).all()
    return users

@app.post("/users/", response_model=User)
async def create_user(user: User):
    db.append(user)
    return user




@app.get("/")
def root():
    return {"message": "Hello World"}


# @app.get("/users")
# async def users():
#
#     return db
