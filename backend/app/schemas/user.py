from enum import Enum
from typing import Optional

from pydantic import BaseModel, EmailStr


class UserRole(str, Enum):
	ADMIN = "admin"
	USER = "user"




class UserBase(BaseModel):
	name: str
	email: EmailStr
	role: UserRole = UserRole.USER
	skills: Optional[str] = None
	interset: Optional[str] = None


class UserCreate(UserBase):
	password: str

class UserLogin(BaseModel):
	email: EmailStr
	password: str


class UserUpdate(BaseModel):
	name: Optional[str] = None
	email: Optional[EmailStr] = None
	role: Optional[UserRole] = None
	skills: Optional[str] = None
	interset: Optional[str] = None


class UserResponse(UserBase):
	id: int
	createdAt: str
	updatedAt: str

	class Config:
		orm_mode = True


class UserInDB(UserResponse):
	hashed_password: str
