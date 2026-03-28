import uuid
from sqlalchemy.orm import Session
from app.models.user import User
from app.schemas.user import UserCreate, UserResponse, UserUpdate, UserLogin
from fastapi import HTTPException, status




class UserRepository:

    def __init__(self, db: Session):
        self.db = db

    def signup(self,name:str,email:str,role:str,skills:str,interest:str,password:str)->UserResponse:
        db_user = User(
            id=str(uuid.uuid4()),
            name=name,
            role=role,
            skills=skills,
            interest=interest,
            email=email,
            password=password,
            created_at=str(uuid.uuid4()),
            updated_at=str(uuid.uuid4())
        )
        self.db.add(db_user)
        self.db.commit()
        self.db.refresh(db_user)
        return db_user

    def login(self, email: str, password: str) -> UserResponse:
        user = self.get_by_email(email)
        if not user or user.password != password:
            raise HTTPException(status_code=401, detail="Invalid email or password")
        return user

    def get_by_email(self, email: str):
        return self.db.query(User).filter(User.email == email).first()

    def create_user(self, email: str, password: str):
        user = User(email=email, password=password)
        self.db.add(user)
        self.db.commit()
        self.db.refresh(user)
        return user