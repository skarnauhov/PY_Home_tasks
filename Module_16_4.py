from fastapi import FastAPI, Path, HTTPException
from typing import Annotated
from pydantic import BaseModel, Field


app = FastAPI()

users = []

class User(BaseModel):
    id: int = Field(..., gt=0, lt=1000,
                    description='User ID', examples=[123,])
    username: str = Field(..., min_length=5, max_length=20,
                          examples=['Вася Пупкин',], description='Enter username')
    age: int = Field(..., ge=18, le=120,
                    description='Enter age', examples=['23',])

@app.get("/")
async def main_page() -> str:
    return "Главная страница"

@app.get("/users")
async def get_users() -> list:
    return users

@app.post("/user/{username}/{age}")
async def create_user(username: Annotated[str, Path(max_length=20, min_length=5,
                     example='Вася Пупкин', description='Enter username')],
                     age: Annotated[int, Path(ge=18, le=120,
                     description='Enter age', example='18')]) -> User:
    user = User(id=len(users)+1, username=username, age=age)
    users.append(user)
    return user

@app.put("/user/{user_id}/{username}/{age}")
async def change_user(user_id: Annotated[int, Path(ge=1, le=1000,
                    description='User ID', example='777')],
                    username: Annotated[str, Path(max_length=20, min_length=5,
                    example='Вася Пупкин', description='Enter username')],
                    age: Annotated[int, Path(ge=18, le=120,
                    description='Enter age', example='18')],
                    ) -> User:
    for user in users:
        if user.id == user_id:
            user.age = age
            user.username = username
            return user
        raise HTTPException(status_code=404, detail='User was not found')

@app.delete("/user/{user_id}")
async def delete_user(user_id: Annotated[int, Path(ge=1, le=1000,
                    description='User ID', example='777')]) -> User:
    index = -1
    for user in users:
        if user.id == user_id:
            index = users.index(user)
    if index >= 0:
        return users.pop(index)
    else:
        raise HTTPException(status_code=404, detail='User was not found')