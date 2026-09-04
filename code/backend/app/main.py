from contextlib import asynccontextmanager
from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from sqlalchemy import text
from app.core.config import settings
from app.db import engine
from app.init_db import init_db

@asynccontextmanager
async def lifespan(app:FastAPI):
 init_db();yield
app=FastAPI(title=settings.app_name,version="0.2.0",description="NABU Personal Operating System API",lifespan=lifespan)
app.add_middleware(CORSMiddleware,allow_origins=settings.cors_list,allow_credentials=True,allow_methods=["*"],allow_headers=["*"])
@app.get("/health")
def health(): return {"status":"ok","service":"nabu-api"}
@app.get("/health/db")
def database_health():
 with engine.connect() as connection: connection.execute(text("SELECT 1"))
 return {"status":"ok","database":"connected"}
from app.routers import auth,goals,projects,tasks,time_entries,skills,income,reviews,research,analytics
app.include_router(auth.router,prefix="/api/v1/auth",tags=["auth"])
app.include_router(goals.router,prefix="/api/v1/goals",tags=["goals"])
app.include_router(projects.router,prefix="/api/v1/projects",tags=["projects"])
app.include_router(tasks.router,prefix="/api/v1/tasks",tags=["tasks"])
app.include_router(skills.router,prefix="/api/v1/skills",tags=["skills"])
app.include_router(time_entries.router,prefix="/api/v1/time-entries",tags=["time"])
app.include_router(income.router,prefix="/api/v1/income",tags=["income"])
app.include_router(reviews.router,prefix="/api/v1/reviews",tags=["reviews"])
app.include_router(research.router,prefix="/api/v1/research",tags=["research"])
app.include_router(analytics.router,prefix="/api/v1/analytics",tags=["analytics"])