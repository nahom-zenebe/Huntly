import enum
from sqlalchemy import Column, Integer, String, Enum, Array,Boolean
from sqlalchemy.orm import sessionmaker
from core.database import Base 


class Status(str,enum.Enum):
    PENDING="pending"
    SUCCESS="success"
    FAILURE="failure"
    PARTIAL="partial"


class ScraperLog:
    __tablename__ = "scraperlogs"

    id=Column(Integer,primary_key=True,index=True)
    sourceId=Column(Integer,nullable=False)
    status=Column(String,nullable=False,default=Status.PENDING)
    message=Column(String,nullable=True)
    scrapcount=Column(Integer,nullable=False,default=0)

    createdAt=Column(String,nullable=False)
    updatedAt=Column(String,nullable=False)