from fastapi import APIRouter, HTTPException, Depends, status
from typing import Annotated
from app.backend.db_depends import get_db
from app.models import *
from sqlalchemy import insert, select, update, delete
from sqlalchemy.orm import Session
from app.schemas import CreateTask, UpdateTask
from slugify import slugify


task_router = APIRouter(prefix="/task", tags=["task"])

@task_router.get("/")
async def all_tasks(db: Annotated[Session, Depends(get_db)]):
    tasks = db.scalars(select(Task).order_by(Task.id)).all()
    return tasks

@task_router.get("/task_id")
async def task_by_id(db: Annotated[Session, Depends(get_db)], task_id: int):
    task = db.scalar(select(Task).where(Task.id == task_id))
    return task

@task_router.post("/create")
async def create_task(db: Annotated[Session, Depends(get_db)], user_id: int, task: CreateTask):
    user = db.scalar(select(User).where(User.id == user_id))

    if user is None:
        raise HTTPException(status_code=404, detail="User not found")

    db.execute(insert(Task).values(user_id=user_id,
                                   title=task.title,
                                   content=task.content,
                                   priority=task.priority,
                                   slug=slugify(task.title)))
    db.commit()
    return {'status_code': status.HTTP_201_CREATED,
            'transaction': 'Task created successfully'}

@task_router.put("/update")
async def update_task(db: Annotated[Session, Depends(get_db)], task_id: int, taskinfo: UpdateTask):
    task = db.scalar(select(Task).where(Task.id == task_id))

    if task is None:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="Task not found")

    db.execute(update(Task).where(Task.id == task_id).values(title=taskinfo.title,
                                   content=taskinfo.content,
                                   priority=taskinfo.priority,
                                   slug=slugify(taskinfo.title)))
    db.commit()
    return {'status_code': status.HTTP_200_OK,
            'transaction': 'Task updated successfully'}

@task_router.delete("/delete")
async def delete_task(db: Annotated[Session, Depends(get_db)], task_id: int):
    task = db.scalar(select(Task).where(Task.id == task_id))

    if task is None:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="Task not found")

    db.execute(delete(Task).where(Task.id == task_id))
    db.commit()

    return {'status_code': status.HTTP_200_OK,
            'transaction': 'Task deleted successfully'}