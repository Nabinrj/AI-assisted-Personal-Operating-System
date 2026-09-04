from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy import select
from sqlalchemy.orm import Session
from app.db import get_db
from app.models import ResearchNote, User
from app.schemas import ResearchCreate, ResearchOut, ResearchUpdate
from app.security import get_current_user
router=APIRouter()
@router.get("",response_model=list[ResearchOut])
def list_notes(user:User=Depends(get_current_user),db:Session=Depends(get_db)): return list(db.scalars(select(ResearchNote).where(ResearchNote.user_id==user.id).order_by(ResearchNote.id.desc())))
@router.post("",response_model=ResearchOut,status_code=201)
def create(payload:ResearchCreate,user:User=Depends(get_current_user),db:Session=Depends(get_db)):
 item=ResearchNote(**payload.model_dump(),user_id=user.id);db.add(item);db.commit();db.refresh(item);return item
@router.patch("/{note_id}",response_model=ResearchOut)
def update(note_id:int,payload:ResearchUpdate,user:User=Depends(get_current_user),db:Session=Depends(get_db)):
 item=db.scalar(select(ResearchNote).where(ResearchNote.id==note_id,ResearchNote.user_id==user.id))
 if not item: raise HTTPException(404,"Research note not found")
 for k,v in payload.model_dump(exclude_unset=True).items(): setattr(item,k,v)
 db.commit();db.refresh(item);return item