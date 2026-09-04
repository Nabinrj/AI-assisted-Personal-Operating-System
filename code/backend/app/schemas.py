from datetime import datetime
from pydantic import BaseModel, ConfigDict, EmailStr, Field

class UserCreate(BaseModel):
    email: EmailStr
    password: str = Field(min_length=8)
    display_name: str = Field(min_length=1, max_length=120)

class UserOut(BaseModel):
    model_config = ConfigDict(from_attributes=True)
    id: int
    email: EmailStr
    display_name: str

class Token(BaseModel):
    access_token: str
    token_type: str = "bearer"

class GoalCreate(BaseModel):
    title: str = Field(min_length=1, max_length=200)
    description: str = ""
    horizon: str = "90-day"
    priority: int = Field(default=3, ge=1, le=5)
    target_date: datetime | None = None
    success_metric: str = ""
    parent_id: int | None = None

class GoalOut(GoalCreate):
    model_config = ConfigDict(from_attributes=True)
    id: int
    user_id: int
    status: str

class ProjectCreate(BaseModel):
    title: str = Field(min_length=1, max_length=200)
    objective: str = ""
    goal_id: int | None = None
    next_action: str = ""
    blocker: str = ""
    repository_url: str = ""

class ProjectOut(ProjectCreate):
    model_config = ConfigDict(from_attributes=True)
    id: int
    user_id: int
    status: str

class TaskCreate(BaseModel):
    title: str = Field(min_length=1, max_length=255)
    project_id: int | None = None
    goal_id: int | None = None
    priority: int = Field(default=3, ge=1, le=5)
    due_at: datetime | None = None
    estimated_minutes: int = Field(default=30, ge=1)

class TaskUpdate(BaseModel):
    status: str | None = None
    completed: bool | None = None
    actual_minutes: int | None = Field(default=None, ge=0)

class TaskOut(TaskCreate):
    model_config = ConfigDict(from_attributes=True)
    id: int
    user_id: int
    status: str
    actual_minutes: int
    completed: bool

from app.schemas_extra import (
    SkillCreate, SkillOut, SkillEvidenceCreate, SkillEvidenceOut,
    TimeEntryCreate, TimeEntryUpdate, TimeEntryOut,
    IncomeCreate, IncomeOut,
    DailyReviewCreate, DailyReviewOut, WeeklyReviewCreate, WeeklyReviewOut,
    ResearchCreate, ResearchUpdate, ResearchOut,
)
