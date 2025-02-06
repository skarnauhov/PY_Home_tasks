from fastapi import FastAPI
from app.routers.task import task_router
from app.routers.user import user_router


app = FastAPI()

@app.get("/")
async def welcome() -> dict:
    return {"message": "Welcome to taskmanager!"}

app.include_router(router=user_router)
app.include_router(router=task_router)

# from sqlalchemy.schema import CreateTable
#
# print(CreateTable(Task.__table__))
# print(CreateTable(User.__table__))