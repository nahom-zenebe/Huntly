from fastapi import HTTPException, status
from sqlalchemy.orm import Session
from app.repository.user import UserRepository
from app.core.security import hash_password, verify_password, create_access_token


class AuthService:

    def __init__(self, db: Session):
        self.repo = UserRepository(db)

    def register(self,name:str,email:str,role:str,skills:str,interest:str,password:str):
        if self.repo.get_by_email(email):
            raise HTTPException(status_code=400, detail="Email already exists")

        hashed = hash_password(password)
        return self.repo.signup(name,email,role,skills,interest,hashed)

    def login(self, email: str, password: str):
        user = self.repo.login(email, password)

        if not user or not verify_password(password, user.password):
            raise HTTPException(status_code=401, detail="Invalid credentials")

        token = create_access_token({"sub": user.id, "role": user.role})

        return {"access_token": token, "token_type": "bearer"}

    def total_user(self):
        return self.repo.total_user()