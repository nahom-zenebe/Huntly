from fastapi import HTTPException, status
from sqlalchemy.orm import Session
from app.repository.user_repository import UserRepository
from app.core.security import hash_password, verify_password, create_access_token


class AuthService:

    def __init__(self, db: Session):
        self.repo = UserRepository(db)

    def register(self, email: str, password: str):
        if self.repo.get_by_email(email):
            raise HTTPException(status_code=400, detail="Email already exists")

        hashed = hash_password(password)
        return self.repo.create_user(email, hashed)

    def login(self, email: str, password: str):
        user = self.repo.get_by_email(email)

        if not user or not verify_password(password, user.password):
            raise HTTPException(status_code=401, detail="Invalid credentials")

        token = create_access_token({"sub": user.id, "role": user.role})

        return {"access_token": token, "token_type": "bearer"}