import uuid
from typing import List

from fastapi import FastAPI
from users.models import User
from users.enums import Gender, Group

app = FastAPI()

# db: List[User] = [
#     User(
#         id=uuid.uuid4(),
#         username='test',
#         first_name='test',
#         last_name='test',
#         gender=Gender.MALE,
#         groups=[Group.user]
#     ),
#     User(
#         id=uuid.uuid4(),
#         username='admin',
#         first_name='admin',
#         last_name='admin',
#         gender=Gender.FEMALE,
#         groups=[Group.admin]
#     )
# ]


@app.get("/")
def root():
    return {"message": "Hello World"}


# @app.get("/users")
# async def users():
#
#     return db
