from fastapi import APIRouter, Depends
from sqlalchemy import select
from sqlalchemy.orm import Session
from app.db import get_db
from app.models import IncomeEntry, User
from app.schemas import IncomeCreate, IncomeOut
from app.security import get_current_user
router=APIRouter()
@router.get("",response_model=list[IncomeOut])
def list_income(user:User=Depends(get_current_user),db:Session=Depends(get_db)):
 return list(db.scalars(select(IncomeEntry).where(IncomeEntry.user_id==user.id).order_by(IncomeEntry.received_at.desc())))
@router.post("",response_model=IncomeOut,status_code=201)
def create(payload:IncomeCreate,user:User=Depends(get_current_user),db:Session=Depends(get_db)):
 item=IncomeEntry(**payload.model_dump(),user_id=user.id);db.add(item);db.commit();db.refresh(item);return item