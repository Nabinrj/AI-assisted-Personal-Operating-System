from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy import select
from sqlalchemy.orm import Session
from app.db import get_db
from app.models import Skill, SkillEvidence, User
from app.schemas import SkillCreate, SkillEvidenceCreate, SkillEvidenceOut, SkillOut
from app.security import get_current_user

router=APIRouter()
@router.get("",response_model=list[SkillOut])
def list_skills(user:User=Depends(get_current_user),db:Session=Depends(get_db)):
 return list(db.scalars(select(Skill).where(Skill.user_id==user.id).order_by(Skill.name)))
@router.post("",response_model=SkillOut,status_code=201)
def create(payload:SkillCreate,user:User=Depends(get_current_user),db:Session=Depends(get_db)):
 item=Skill(**payload.model_dump(),user_id=user.id);db.add(item);db.commit();db.refresh(item);return item
@router.post("/{skill_id}/evidence",response_model=SkillEvidenceOut,status_code=201)
def evidence(skill_id:int,payload:SkillEvidenceCreate,user:User=Depends(get_current_user),db:Session=Depends(get_db)):
 skill=db.scalar(select(Skill).where(Skill.id==skill_id,Skill.user_id==user.id))
 if not skill: raise HTTPException(404,"Skill not found")
 item=SkillEvidence(**payload.model_dump(),skill_id=skill.id);db.add(item);db.commit();db.refresh(item);return item
@router.get("/{skill_id}/evidence",response_model=list[SkillEvidenceOut])
def list_evidence(skill_id:int,user:User=Depends(get_current_user),db:Session=Depends(get_db)):
 skill=db.scalar(select(Skill).where(Skill.id==skill_id,Skill.user_id==user.id))
 if not skill: raise HTTPException(404,"Skill not found")
 return list(db.scalars(select(SkillEvidence).where(SkillEvidence.skill_id==skill.id)))