from datetime import date, datetime
from sqlalchemy import String, Text, DateTime, Date, Integer, ForeignKey, Boolean, Numeric
from sqlalchemy.orm import Mapped, mapped_column, relationship
from app.db import Base

class User(Base):
    __tablename__="users"
    id:Mapped[int]=mapped_column(primary_key=True);email:Mapped[str]=mapped_column(String(255),unique=True,index=True);password_hash:Mapped[str]=mapped_column(String(255));display_name:Mapped[str]=mapped_column(String(120));created_at:Mapped[datetime]=mapped_column(DateTime,default=datetime.utcnow)
    goals=relationship("Goal",back_populates="user",cascade="all, delete-orphan");tasks=relationship("Task",back_populates="user",cascade="all, delete-orphan");projects=relationship("Project",back_populates="user",cascade="all, delete-orphan")
class Goal(Base):
    __tablename__="goals"
    id:Mapped[int]=mapped_column(primary_key=True);user_id:Mapped[int]=mapped_column(ForeignKey("users.id"),index=True);parent_id:Mapped[int|None]=mapped_column(ForeignKey("goals.id"),nullable=True);title:Mapped[str]=mapped_column(String(200));description:Mapped[str]=mapped_column(Text,default="");horizon:Mapped[str]=mapped_column(String(30),default="90-day");status:Mapped[str]=mapped_column(String(30),default="active");priority:Mapped[int]=mapped_column(Integer,default=3);target_date:Mapped[datetime|None]=mapped_column(DateTime,nullable=True);success_metric:Mapped[str]=mapped_column(String(255),default="");user=relationship("User",back_populates="goals")
class Project(Base):
    __tablename__="projects"
    id:Mapped[int]=mapped_column(primary_key=True);user_id:Mapped[int]=mapped_column(ForeignKey("users.id"),index=True);goal_id:Mapped[int|None]=mapped_column(ForeignKey("goals.id"),nullable=True);title:Mapped[str]=mapped_column(String(200));objective:Mapped[str]=mapped_column(Text,default="");status:Mapped[str]=mapped_column(String(30),default="active");next_action:Mapped[str]=mapped_column(String(255),default="");blocker:Mapped[str]=mapped_column(String(255),default="");repository_url:Mapped[str]=mapped_column(String(500),default="");user=relationship("User",back_populates="projects")
class Task(Base):
    __tablename__="tasks"
    id:Mapped[int]=mapped_column(primary_key=True);user_id:Mapped[int]=mapped_column(ForeignKey("users.id"),index=True);project_id:Mapped[int|None]=mapped_column(ForeignKey("projects.id"),nullable=True);goal_id:Mapped[int|None]=mapped_column(ForeignKey("goals.id"),nullable=True);title:Mapped[str]=mapped_column(String(255));status:Mapped[str]=mapped_column(String(30),default="todo");priority:Mapped[int]=mapped_column(Integer,default=3);due_at:Mapped[datetime|None]=mapped_column(DateTime,nullable=True);estimated_minutes:Mapped[int]=mapped_column(Integer,default=30);actual_minutes:Mapped[int]=mapped_column(Integer,default=0);completed:Mapped[bool]=mapped_column(Boolean,default=False);user=relationship("User",back_populates="tasks")
class Skill(Base):
    __tablename__="skills"
    id:Mapped[int]=mapped_column(primary_key=True);user_id:Mapped[int]=mapped_column(ForeignKey("users.id"),index=True);name:Mapped[str]=mapped_column(String(120));current_level:Mapped[int]=mapped_column(Integer,default=1);target_level:Mapped[int]=mapped_column(Integer,default=5)
class SkillEvidence(Base):
    __tablename__="skill_evidence"
    id:Mapped[int]=mapped_column(primary_key=True);skill_id:Mapped[int]=mapped_column(ForeignKey("skills.id"),index=True);description:Mapped[str]=mapped_column(Text);url:Mapped[str]=mapped_column(String(500),default="");completed_at:Mapped[datetime]=mapped_column(DateTime,default=datetime.utcnow)
class TimeEntry(Base):
    __tablename__="time_entries"
    id:Mapped[int]=mapped_column(primary_key=True);user_id:Mapped[int]=mapped_column(ForeignKey("users.id"),index=True);category:Mapped[str]=mapped_column(String(60));started_at:Mapped[datetime]=mapped_column(DateTime);duration_minutes:Mapped[int]=mapped_column(Integer);note:Mapped[str]=mapped_column(Text,default="")
class IncomeEntry(Base):
    __tablename__="income_entries"
    id:Mapped[int]=mapped_column(primary_key=True);user_id:Mapped[int]=mapped_column(ForeignKey("users.id"),index=True);source:Mapped[str]=mapped_column(String(120));amount:Mapped[float]=mapped_column(Numeric(12,2));currency:Mapped[str]=mapped_column(String(8),default="NPR");received_at:Mapped[datetime]=mapped_column(DateTime,default=datetime.utcnow);note:Mapped[str]=mapped_column(Text,default="")
class DailyReview(Base):
    __tablename__="daily_reviews"
    id:Mapped[int]=mapped_column(primary_key=True);user_id:Mapped[int]=mapped_column(ForeignKey("users.id"),index=True);review_date:Mapped[date]=mapped_column(Date,default=date.today);completed_summary:Mapped[str]=mapped_column(Text,default="");blocker:Mapped[str]=mapped_column(Text,default="");tomorrow_priority:Mapped[str]=mapped_column(String(255),default="")
class WeeklyReview(Base):
    __tablename__="weekly_reviews"
    id:Mapped[int]=mapped_column(primary_key=True);user_id:Mapped[int]=mapped_column(ForeignKey("users.id"),index=True);week_start:Mapped[date]=mapped_column(Date);wins:Mapped[str]=mapped_column(Text,default="");failures:Mapped[str]=mapped_column(Text,default="");lessons:Mapped[str]=mapped_column(Text,default="");next_week_priority:Mapped[str]=mapped_column(String(255),default="")
class ResearchNote(Base):
    __tablename__="research_notes"
    id:Mapped[int]=mapped_column(primary_key=True);user_id:Mapped[int]=mapped_column(ForeignKey("users.id"),index=True);question:Mapped[str]=mapped_column(String(500));hypothesis:Mapped[str]=mapped_column(Text,default="");experiment:Mapped[str]=mapped_column(Text,default="");result:Mapped[str]=mapped_column(Text,default="");conclusion:Mapped[str]=mapped_column(Text,default="");status:Mapped[str]=mapped_column(String(30),default="active")