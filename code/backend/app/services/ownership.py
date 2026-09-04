from fastapi import HTTPException
from sqlalchemy import select
from sqlalchemy.orm import Session
from app.models import Goal, Project, Task, User

def owned_goal(db:Session,user:User,goal_id:int)->Goal:
 item=db.scalar(select(Goal).where(Goal.id==goal_id,Goal.user_id==user.id))
 if not item: raise HTTPException(404,"Goal not found")
 return item

def owned_project(db:Session,user:User,project_id:int)->Project:
 item=db.scalar(select(Project).where(Project.id==project_id,Project.user_id==user.id))
 if not item: raise HTTPException(404,"Project not found")
 return item

def owned_task(db:Session,user:User,task_id:int)->Task:
 item=db.scalar(select(Task).where(Task.id==task_id,Task.user_id==user.id))
 if not item: raise HTTPException(404,"Task not found")
 return item