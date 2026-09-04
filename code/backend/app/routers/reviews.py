from fastapi import APIRouter, Depends
from sqlalchemy import select
from sqlalchemy.orm import Session
from app.db import get_db
from app.models import DailyReview, WeeklyReview, User
from app.schemas import DailyReviewCreate, DailyReviewOut, WeeklyReviewCreate, WeeklyReviewOut
from app.security import get_current_user
router=APIRouter()
@router.get("/daily",response_model=list[DailyReviewOut])
def daily_list(user:User=Depends(get_current_user),db:Session=Depends(get_db)): return list(db.scalars(select(DailyReview).where(DailyReview.user_id==user.id).order_by(DailyReview.review_date.desc())))
@router.post("/daily",response_model=DailyReviewOut,status_code=201)
def daily_create(payload:DailyReviewCreate,user:User=Depends(get_current_user),db:Session=Depends(get_db)):
 item=DailyReview(**payload.model_dump(),user_id=user.id);db.add(item);db.commit();db.refresh(item);return item
@router.get("/weekly",response_model=list[WeeklyReviewOut])
def weekly_list(user:User=Depends(get_current_user),db:Session=Depends(get_db)): return list(db.scalars(select(WeeklyReview).where(WeeklyReview.user_id==user.id).order_by(WeeklyReview.week_start.desc())))
@router.post("/weekly",response_model=WeeklyReviewOut,status_code=201)
def weekly_create(payload:WeeklyReviewCreate,user:User=Depends(get_current_user),db:Session=Depends(get_db)):
 item=WeeklyReview(**payload.model_dump(),user_id=user.id);db.add(item);db.commit();db.refresh(item);return item