from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session
from app.schemas.user import UserCreate, UserLogin
from app.services.auth_service import AuthService
from app.api.deps import get_db

router = APIRouter(prefix="/auth", tags=["Auth"])


@router.post("/register")
def register(user: UserCreate, db: Session = Depends(get_db)):
    service = AuthService(db)
    return service.register(user.email, user.password)


@router.post("/login")
def login(user: UserLogin, db: Session = Depends(get_db)):
    service = AuthService(db)
    return service.login(user.email, user.password)


@router.post("/logout")
def logout():
    return {"message": "Logout successful (client should delete token)"}