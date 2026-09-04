from fastapi import APIRouter, Depends
from sqlalchemy import select
from sqlalchemy.orm import Session
from app.db import get_db
from app.models import Task, User
from app.schemas import TaskCreate, TaskUpdate, TaskOut
from app.security import get_current_user
from app.services.ownership import owned_goal, owned_project, owned_task
router=APIRouter()
@router.get("",response_model=list[TaskOut])
def list_tasks(user:User=Depends(get_current_user),db:Session=Depends(get_db)): return list(db.scalars(select(Task).where(Task.user_id==user.id).order_by(Task.completed,Task.priority,Task.id.desc())))
@router.post("",response_model=TaskOut,status_code=201)
def create_task(payload:TaskCreate,user:User=Depends(get_current_user),db:Session=Depends(get_db)):
 if payload.goal_id: owned_goal(db,user,payload.goal_id)
 if payload.project_id: owned_project(db,user,payload.project_id)
 item=Task(**payload.model_dump(),user_id=user.id);db.add(item);db.commit();db.refresh(item);return item
@router.patch("/{task_id}",response_model=TaskOut)
def update_task(task_id:int,payload:TaskUpdate,user:User=Depends(get_current_user),db:Session=Depends(get_db)):
 item=owned_task(db,user,task_id)
 for k,v in payload.model_dump(exclude_unset=True).items(): setattr(item,k,v)
 if payload.completed is True: item.status="done"
 elif payload.completed is False and item.status=="done": item.status="todo"
 db.commit();db.refresh(item);return item
@router.delete("/{task_id}",status_code=204)
def delete_task(task_id:int,user:User=Depends(get_current_user),db:Session=Depends(get_db)):
 item=owned_task(db,user,task_id);db.delete(item);db.commit()