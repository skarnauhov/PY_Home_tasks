from fastapi import APIRouter, HTTPException, Depends, status
from typing import Annotated
from app.backend.db_depends import get_db
from app.models import *
from sqlalchemy import insert, select, update, delete
from sqlalchemy.orm import Session
from app.schemas import CreateUser, UpdateUser
from slugify import slugify


user_router = APIRouter(prefix="/user", tags=["user"])

@user_router.get("/")
async def all_users(db: Annotated[Session, Depends(get_db)]):
    users = db.scalars(select(User).order_by(User.id)).all()
    return users

@user_router.get("/user_id")
async def user_by_id(db: Annotated[Session, Depends(get_db)], user_id: int):
    user = db.scalar(select(User).where(User.id == user_id))

    if user is None:
        raise HTTPException(status_code=404, detail="User not found")

    return user

@user_router.get("/user_id/tasks")
async def tasks_by_user_id(db: Annotated[Session, Depends(get_db)], user_id: int):
    user = db.scalar(select(User).where(User.id == user_id))

    if user is None:
        raise HTTPException(status_code=404, detail="User not found")

    tasks = db.scalars(select(Task).where(Task.user_id==user_id).order_by(Task.id)).all()
    return tasks

@user_router.post("/create")
async def create_user(db: Annotated[Session, Depends(get_db)], user: CreateUser):
    db.execute(insert(User).values(username=user.username,
                                   firstname=user.firstname,
                                   lastname=user.lastname,
                                   age=user.age,
                                   slug=slugify(user.username)))
    db.commit()
    return {'status_code': status.HTTP_201_CREATED,
            'transaction': 'User created successfully'}

@user_router.put("/update")
async def update_user(db: Annotated[Session, Depends(get_db)], user_id: int, userinfo: UpdateUser):
    user = db.scalar(select(User).where(User.id == user_id))

    if user is None:
        raise HTTPException(status_code=404, detail="User not found")

    db.execute(update(User).where(User.id==user_id).values(firstname=userinfo.firstname,
                                   lastname=userinfo.lastname,
                                   age=userinfo.age))
    db.commit()
    return {'status_code': status.HTTP_200_OK,
            'transaction': 'User updated successfully'}

@user_router.delete("/delete")
async def delete_user(db: Annotated[Session, Depends(get_db)], user_id: int):
    user = db.scalar(select(User).where(User.id == user_id))

    if user is None:
        raise HTTPException(status_code=404, detail="User not found")

    db.execute(delete(User).where(User.id == user_id))
    db.execute(delete(Task).where(Task.user_id == user_id))
    db.commit()
    return {'status_code': status.HTTP_200_OK,
            'transaction': 'User and his tasks deleted successfully'}
