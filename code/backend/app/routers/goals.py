from fastapi import APIRouter, Depends
from sqlalchemy import select
from sqlalchemy.orm import Session
from app.db import get_db
from app.models import Goal, User
from app.schemas import GoalCreate, GoalOut
from app.security import get_current_user

router = APIRouter()

@router.get("", response_model=list[GoalOut])
def list_goals(user: User = Depends(get_current_user), db: Session = Depends(get_db)):
    return list(db.scalars(select(Goal).where(Goal.user_id == user.id).order_by(Goal.priority, Goal.id)))

@router.post("", response_model=GoalOut, status_code=201)
def create_goal(payload: GoalCreate, user: User = Depends(get_current_user), db: Session = Depends(get_db)):
    goal = Goal(**payload.model_dump(), user_id=user.id)
    db.add(goal); db.commit(); db.refresh(goal)
    return goal
