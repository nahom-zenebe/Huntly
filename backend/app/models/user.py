import enum
from sqlalchemy import Column, Integer, String, Enum
from sqlalchemy.orm import sessionmaker
from core.database import Base 

class UserRole(str, enum.Enum): 
    ADMIN = "admin"
    USER = "user"

class User(Base):
    __tablename__ = "users"

    id = Column(Integer, primary_key=True, index=True)
    name = Column(String, index=True, nullable=False) 
    email = Column(String, unique=True, index=True, nullable=False)
    hashed_password = Column(String, nullable=False)
    role = Column(Enum(UserRole), default=UserRole.USER) 
    skills=Column(String, nullable=True)
    interset=Column(String, nullable=True)
    createdAt=Column(String, nullable=False)
    updatedAt=Column(String, nullable=False)
