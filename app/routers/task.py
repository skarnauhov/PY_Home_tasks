from fastapi import APIRouter
from pydantic import BaseModel

task_router = APIRouter(prefix="/task", tags=["task"])

class Task(BaseModel):
    pass

@task_router.get("/")
async def all_tasks():
    pass

@task_router.get("/task_id")
async def task_by_id(task_id: int):
    pass

@task_router.post("/create")
async def create_task(task: Task):
    pass

@task_router.put("/update")
async def update_task(task: Task):
    pass

@task_router.delete("/delete")
async def delete_task(task: Task):
    pass