from datetime import datetime
from sqlalchemy import String, Text, DateTime, Integer, ForeignKey, Boolean
from sqlalchemy.orm import Mapped, mapped_column, relationship
from app.db import Base

class User(Base):
    __tablename__ = "users"
    id: Mapped[int] = mapped_column(primary_key=True)
    email: Mapped[str] = mapped_column(String(255), unique=True, index=True)
    password_hash: Mapped[str] = mapped_column(String(255))
    display_name: Mapped[str] = mapped_column(String(120))
    created_at: Mapped[datetime] = mapped_column(DateTime, default=datetime.utcnow)
    goals = relationship("Goal", back_populates="user", cascade="all, delete-orphan")
    tasks = relationship("Task", back_populates="user", cascade="all, delete-orphan")
    projects = relationship("Project", back_populates="user", cascade="all, delete-orphan")

class Goal(Base):
    __tablename__ = "goals"
    id: Mapped[int] = mapped_column(primary_key=True)
    user_id: Mapped[int] = mapped_column(ForeignKey("users.id"), index=True)
    parent_id: Mapped[int | None] = mapped_column(ForeignKey("goals.id"), nullable=True)
    title: Mapped[str] = mapped_column(String(200))
    description: Mapped[str] = mapped_column(Text, default="")
    horizon: Mapped[str] = mapped_column(String(30), default="90-day")
    status: Mapped[str] = mapped_column(String(30), default="active")
    priority: Mapped[int] = mapped_column(Integer, default=3)
    target_date: Mapped[datetime | None] = mapped_column(DateTime, nullable=True)
    success_metric: Mapped[str] = mapped_column(String(255), default="")
    user = relationship("User", back_populates="goals")

class Project(Base):
    __tablename__ = "projects"
    id: Mapped[int] = mapped_column(primary_key=True)
    user_id: Mapped[int] = mapped_column(ForeignKey("users.id"), index=True)
    goal_id: Mapped[int | None] = mapped_column(ForeignKey("goals.id"), nullable=True)
    title: Mapped[str] = mapped_column(String(200))
    objective: Mapped[str] = mapped_column(Text, default="")
    status: Mapped[str] = mapped_column(String(30), default="active")
    next_action: Mapped[str] = mapped_column(String(255), default="")
    blocker: Mapped[str] = mapped_column(String(255), default="")
    repository_url: Mapped[str] = mapped_column(String(500), default="")
    user = relationship("User", back_populates="projects")

class Task(Base):
    __tablename__ = "tasks"
    id: Mapped[int] = mapped_column(primary_key=True)
    user_id: Mapped[int] = mapped_column(ForeignKey("users.id"), index=True)
    project_id: Mapped[int | None] = mapped_column(ForeignKey("projects.id"), nullable=True)
    goal_id: Mapped[int | None] = mapped_column(ForeignKey("goals.id"), nullable=True)
    title: Mapped[str] = mapped_column(String(255))
    status: Mapped[str] = mapped_column(String(30), default="todo")
    priority: Mapped[int] = mapped_column(Integer, default=3)
    due_at: Mapped[datetime | None] = mapped_column(DateTime, nullable=True)
    estimated_minutes: Mapped[int] = mapped_column(Integer, default=30)
    actual_minutes: Mapped[int] = mapped_column(Integer, default=0)
    completed: Mapped[bool] = mapped_column(Boolean, default=False)
    user = relationship("User", back_populates="tasks")
