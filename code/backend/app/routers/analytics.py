from datetime import datetime, timedelta
from fastapi import APIRouter, Depends
from sqlalchemy import func, select
from sqlalchemy.orm import Session
from app.db import get_db
from app.models import Goal, IncomeEntry, Project, Task, TimeEntry, User
from app.security import get_current_user
router=APIRouter()
@router.get("/dashboard")
def dashboard(user:User=Depends(get_current_user),db:Session=Depends(get_db)):
 tasks=list(db.scalars(select(Task).where(Task.user_id==user.id)))
 total=len(tasks); completed=sum(1 for t in tasks if t.completed)
 week=datetime.utcnow()-timedelta(days=7)
 time_rows=db.execute(select(TimeEntry.category,func.coalesce(func.sum(TimeEntry.duration_minutes),0)).where(TimeEntry.user_id==user.id,TimeEntry.started_at>=week).group_by(TimeEntry.category)).all()
 income=db.scalar(select(func.coalesce(func.sum(IncomeEntry.amount),0)).where(IncomeEntry.user_id==user.id)) or 0
 return {"tasks_total":total,"tasks_completed":completed,"execution_rate":round(completed/total*100,1) if total else 0,"goals_active":db.scalar(select(func.count()).select_from(Goal).where(Goal.user_id==user.id,Goal.status=="active")) or 0,"projects_active":db.scalar(select(func.count()).select_from(Project).where(Project.user_id==user.id,Project.status=="active")) or 0,"income_total":float(income),"time_by_category":[{"category":c,"minutes":int(m)} for c,m in time_rows]}
@router.get("/reality-check")
def reality_check(user:User=Depends(get_current_user),db:Session=Depends(get_db)):
 tasks=list(db.scalars(select(Task).where(Task.user_id==user.id)))
 planned=sum(t.estimated_minutes for t in tasks); actual=sum(t.actual_minutes for t in tasks); completed=sum(1 for t in tasks if t.completed)
 alerts=[]
 if tasks and completed==0: alerts.append({"severity":"high","message":"You have planned work but no completed tasks. Execution is the bottleneck."})
 if planned>0 and actual<planned*.5: alerts.append({"severity":"medium","message":"Logged effort is below half of planned effort."})
 if not alerts: alerts.append({"severity":"info","message":"No deterministic contradiction detected from the current data."})
 return {"planned_minutes":planned,"actual_minutes":actual,"alerts":alerts}