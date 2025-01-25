from fastapi import FastAPI, Path
from typing import Annotated


app = FastAPI()

@app.get("/")
async def main_page() -> str:
    return "Главная страница"

@app.get("/user/admin")
async def admin_page() -> str:
    return "Вы вошли как администратор"

@app.get("/user/{user_id}")
async def user_page(user_id: Annotated[int, Path(ge=1, le=100, description='Enter user ID', examples=['88',])]) -> str:
    return f"Вы вошли как пользователь №: {user_id}"

@app.get("/user/{user_name}/{user_age}")
async def user_info(user_name: Annotated[str, Path(max_length=20, min_length=5,
                                                   example='Вася Пупкин', description='Enter username')],
                    user_age: Annotated[int, Path(ge=18, le=120, description='Enter age', example='18')]) -> str:
    return f"Информация о пользователе. Имя: {user_name}, Возраст: {user_age}"