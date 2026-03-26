import enum
from sqlalchemy import Column, Integer, String, Enum, Array,Boolean
from sqlalchemy.orm import sessionmaker
from core.database import Base 


class Type(str,enum.Enum):
    APPLICATION_UPDATE="application_update"
    NEW_OPPORTUNITY="new_opportunity"
    GENERAL="general"


class Notification:
    __tablename__ = "notifications"

    id=Column(Integer,primary_key=True,index=True)
    userId=Column(Integer,nullable=False)
    title=Column(String,nullable=False)
    message=Column(String,nullable=False)
    isRead=Column(Boolean,nullable=False,default=False)
    type=Column(String,default=Type.GENERAL)
    createdAt=Column(String,nullable=False)
    updatedAt=Column(String,nullable=False)