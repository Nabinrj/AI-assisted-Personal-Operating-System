from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy import select
from sqlalchemy.orm import Session
from app.db import get_db
from app.models import TimeEntry, User
from app.schemas import TimeEntryCreate, TimeEntryOut, TimeEntryUpdate
from app.security import get_current_user

router=APIRouter()
@router.get("",response_model=list[TimeEntryOut])
def list_entries(user:User=Depends(get_current_user),db:Session=Depends(get_db)):
    return list(db.scalars(select(TimeEntry).where(TimeEntry.user_id==user.id).order_by(TimeEntry.started_at.desc())))
@router.post("",response_model=TimeEntryOut,status_code=201)
def create(payload:TimeEntryCreate,user:User=Depends(get_current_user),db:Session=Depends(get_db)):
    item=TimeEntry(**payload.model_dump(),user_id=user.id);db.add(item);db.commit();db.refresh(item);return item
@router.patch("/{entry_id}",response_model=TimeEntryOut)
def update(entry_id:int,payload:TimeEntryUpdate,user:User=Depends(get_current_user),db:Session=Depends(get_db)):
    item=db.scalar(select(TimeEntry).where(TimeEntry.id==entry_id,TimeEntry.user_id==user.id))
    if not item: raise HTTPException(404,"Time entry not found")
    for k,v in payload.model_dump(exclude_unset=True).items(): setattr(item,k,v)
    db.commit();db.refresh(item);return item
@router.delete("/{entry_id}",status_code=204)
def delete(entry_id:int,user:User=Depends(get_current_user),db:Session=Depends(get_db)):
    item=db.scalar(select(TimeEntry).where(TimeEntry.id==entry_id,TimeEntry.user_id==user.id))
    if not item: raise HTTPException(404,"Time entry not found")
    db.delete(item);db.commit()