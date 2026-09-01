from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy import select
from sqlalchemy.orm import Session
from app.db import get_db
from app.models import Task, User
from app.schemas import TaskCreate, TaskUpdate, TaskOut
from app.security import get_current_user

router = APIRouter()

@router.get("", response_model=list[TaskOut])
def list_tasks(user: User = Depends(get_current_user), db: Session = Depends(get_db)):
    return list(db.scalars(select(Task).where(Task.user_id == user.id).order_by(Task.completed, Task.priority, Task.id.desc())))

@router.post("", response_model=TaskOut, status_code=201)
def create_task(payload: TaskCreate, user: User = Depends(get_current_user), db: Session = Depends(get_db)):
    task = Task(**payload.model_dump(), user_id=user.id)
    db.add(task); db.commit(); db.refresh(task)
    return task

@router.patch("/{task_id}", response_model=TaskOut)
def update_task(task_id: int, payload: TaskUpdate, user: User = Depends(get_current_user), db: Session = Depends(get_db)):
    task = db.scalar(select(Task).where(Task.id == task_id, Task.user_id == user.id))
    if not task:
        raise HTTPException(404, "Task not found")
    for key, value in payload.model_dump(exclude_unset=True).items():
        setattr(task, key, value)
    if payload.completed is True:
        task.status = "done"
    db.commit(); db.refresh(task)
    return task
