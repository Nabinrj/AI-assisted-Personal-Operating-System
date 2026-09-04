from fastapi import APIRouter, Depends
from sqlalchemy import select
from sqlalchemy.orm import Session
from app.db import get_db
from app.models import Project, User
from app.schemas import ProjectCreate, ProjectOut
from app.security import get_current_user
from app.services.ownership import owned_goal, owned_project
router=APIRouter()
@router.get("",response_model=list[ProjectOut])
def list_projects(user:User=Depends(get_current_user),db:Session=Depends(get_db)): return list(db.scalars(select(Project).where(Project.user_id==user.id).order_by(Project.id.desc())))
@router.post("",response_model=ProjectOut,status_code=201)
def create_project(payload:ProjectCreate,user:User=Depends(get_current_user),db:Session=Depends(get_db)):
 if payload.goal_id: owned_goal(db,user,payload.goal_id)
 item=Project(**payload.model_dump(),user_id=user.id);db.add(item);db.commit();db.refresh(item);return item
@router.patch("/{project_id}",response_model=ProjectOut)
def update_project(project_id:int,payload:ProjectCreate,user:User=Depends(get_current_user),db:Session=Depends(get_db)):
 item=owned_project(db,user,project_id)
 if payload.goal_id: owned_goal(db,user,payload.goal_id)
 for k,v in payload.model_dump().items(): setattr(item,k,v)
 db.commit();db.refresh(item);return item
@router.delete("/{project_id}",status_code=204)
def delete_project(project_id:int,user:User=Depends(get_current_user),db:Session=Depends(get_db)):
 item=owned_project(db,user,project_id);db.delete(item);db.commit()