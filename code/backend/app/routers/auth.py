from fastapi import APIRouter, Depends, HTTPException, status
from fastapi.security import OAuth2PasswordRequestForm
from sqlalchemy import select
from sqlalchemy.orm import Session
from app.db import get_db
from app.models import User
from app.schemas import UserCreate, UserOut, Token
from app.security import hash_password, verify_password, create_access_token, get_current_user

router = APIRouter()

@router.post("/register", response_model=UserOut, status_code=201)
def register(payload: UserCreate, db: Session = Depends(get_db)):
    if db.scalar(select(User).where(User.email == payload.email.lower())):
        raise HTTPException(409, "Email already registered")
    user = User(email=payload.email.lower(), password_hash=hash_password(payload.password), display_name=payload.display_name)
    db.add(user); db.commit(); db.refresh(user)
    return user

@router.post("/login", response_model=Token)
def login(form: OAuth2PasswordRequestForm = Depends(), db: Session = Depends(get_db)):
    user = db.scalar(select(User).where(User.email == form.username.lower()))
    if not user or not verify_password(form.password, user.password_hash):
        raise HTTPException(status.HTTP_401_UNAUTHORIZED, "Incorrect email or password")
    return Token(access_token=create_access_token(user.id))

@router.get("/me", response_model=UserOut)
def me(user: User = Depends(get_current_user)):
    return user
