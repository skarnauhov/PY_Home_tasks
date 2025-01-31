from fastapi import FastAPI, Path, HTTPException, Request, Form
from typing import Annotated
from pydantic import BaseModel, Field
from fastapi.templating import Jinja2Templates
from fastapi.responses import HTMLResponse
from starlette import status

app = FastAPI(swagger_ui_parameters={"tryItOutEnabled": True}, debug=True)

templates = Jinja2Templates(directory="templates")


class User(BaseModel):
    id: int = Field(..., gt=0, lt=1000,
                    description='User ID', examples=[123,])
    username: str = Field(..., min_length=5, max_length=20,
                          examples=['Вася Пупкин',], description='Enter username')
    age: int = Field(..., ge=18, le=120,
                    description='Enter age', examples=['23',])

users = [User(id=1, username='UrbanUser', age=24),
         User(id=2, username='UrbanTest', age=22),
         User(id=3, username='Capybara', age=60)
         ]

@app.get("/")
async def main_page(request: Request) -> HTMLResponse:
    return templates.TemplateResponse("users.html", {"request": request, "users": users})

@app.get("/user/{user_id}")
async def get_user(request: Request, user_id: int) ->HTMLResponse:
    for user in users:
        if user.id == user_id:
            return templates.TemplateResponse("users.html", {"request": request, "user": user})
    raise HTTPException(status_code=404, detail="User not found")

@app.post("/", status_code=status.HTTP_201_CREATED)
async def create_user(request: Request, username: str = Form(), age: int = Form()) -> HTMLResponse:
    user = User(id=len(users)+1, username=username, age=age)
    users.append(user)
    return templates.TemplateResponse("users.html", {"request": request, "users": users})

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


@app.put("/user/{user_id}/{username}/{age}")
async def change_user(user_id: Annotated[int, Path(ge=1, le=1000,
                    description='User ID', example='777')],
                    username: Annotated[str, Path(max_length=20, min_length=5,
                    example='Вася Пупкин', description='Enter username')],
                    age: Annotated[int, Path(ge=18, le=120,
                    description='Enter age', example='18')],
                    ) -> User:
    for user in users:
        if user.id == int(user_id):
            user.age = age
            user.username = username
            return user
    raise HTTPException(status_code=404, detail='User was not found')