from fastapi import APIRouter
from pydantic import BaseModel

user_router = APIRouter(prefix="/user", tags=["user"])

class User(BaseModel):
    pass

@user_router.get("/")
async def all_users():
    pass

@user_router.get("/user_id")
async def user_by_id(user_id: int):
    pass

@user_router.post("/create")
async def create_user(user: User):
    pass

@user_router.put("/update")
async def update_user(user: User):
    pass

@user_router.delete("/delete")
async def delete_user(user: User):
    pass
