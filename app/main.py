from fastapi import FastAPI
from routers.task import task_router
from routers.user import user_router
import schemas

app = FastAPI()

@app.get("/")
async def welcome() -> dict:
    return {"message": "Welcome to taskmanager!"}

app.include_router(router=user_router)
app.include_router(router=task_router)