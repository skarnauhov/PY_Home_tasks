from fastapi import FastAPI, Path
from typing import Annotated


app = FastAPI()

users = {'1': 'Имя: Example+, возраст: 18'}

@app.get("/")
async def main_page() -> str:
    return "Главная страница"

@app.get("/users")
async def get_users() -> dict:
    return users

@app.post("/user/{username}/{age}")

async def create_user(username: Annotated[str, Path(max_length=20, min_length=5,
                    example='Вася Пупкин', description='Enter username')],
                    age: Annotated[int, Path(ge=18, le=120,
                    description='Enter age', example='18')]) -> str:
    user_id = str(int(max(users, key=int)) + 1)
    users[user_id] = f'Имя: {username}, возраст: {age}'
    return f"User {user_id} is registered"

@app.put("/user/{user_id}/{username}/{age}")
async def change_user(user_id: Annotated[int, Path(ge=1, le=1000,
                    description='User ID', example='777')],
                    username: Annotated[str, Path(max_length=20, min_length=5,
                    example='Вася Пупкин', description='Enter username')],
                    age: Annotated[int, Path(ge=18, le=120,
                    description='Enter age', example='18')],
                    ) -> str:
    users[str(user_id)] = f'Имя: {username}, возраст: {age}'
    return f"User {user_id} has been updated"

@app.delete("/user/{user_id}")
async def delete_user(user_id: Annotated[int, Path(ge=1, le=1000,
                    description='User ID', example='777')]) -> str:
    users.pop(str(user_id))
    return f"User {user_id} has been deleted"