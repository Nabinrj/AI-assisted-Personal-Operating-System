from fastapi import APIRouter, Depends
from sqlalchemy import select
from sqlalchemy.orm import Session
from app.db import get_db
from app.models import Project, User
from app.schemas import ProjectCreate, ProjectOut
from app.security import get_current_user

router = APIRouter()

@router.get("", response_model=list[ProjectOut])
def list_projects(user: User = Depends(get_current_user), db: Session = Depends(get_db)):
    return list(db.scalars(select(Project).where(Project.user_id == user.id).order_by(Project.id.desc())))

@router.post("", response_model=ProjectOut, status_code=201)
def create_project(payload: ProjectCreate, user: User = Depends(get_current_user), db: Session = Depends(get_db)):
    project = Project(**payload.model_dump(), user_id=user.id)
    db.add(project); db.commit(); db.refresh(project)
    return project
