from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session
from app.schemas.user import UserCreate, UserLogin
from app.services.user_service import AuthService
from app.api.deps import get_db

router = APIRouter(prefix="/auth", tags=["Auth"])


@router.post("/register")
def register(user: UserCreate, db: Session = Depends(get_db)):
    service = AuthService(db)
    return service.register(user.name, user.email, user.role, user.skills, user.interest, user.password)


@router.post("/login")
def login(user: UserLogin, db: Session = Depends(get_db)):
    service = AuthService(db)
    return service.login(user.email, user.password)

@router.get("/total-users")
def total_users(db: Session = Depends(get_db)):
    service = AuthService(db)
    return service.total_user()

@router.post("/logout")
def logout():
    return {"message": "Logout successful (client should delete token)"}