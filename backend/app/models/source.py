import enum
from sqlalchemy import Column, Integer, String, Enum, Array,Boolean
from sqlalchemy.orm import sessionmaker
from core.database import Base 


 
class SourceType(str,enum.Enum):
    JOB="job"
    HACKATHON="hackathon"
    GENERAL="general"


class Source:
    __tablename__ = "sources"

    id=Column(Integer,primary_key=True,index=True)
    name=Column(String,index=True,nullable=False)
    baseUrl=Column(String,nullable=False)
    type=Column(Enum(SourceType),nullable=False)

    isActive=Column(Boolean,nullable=False,default=True)
    lastScrapedAt=Column(String,nullable=True)
    createdAt=Column(String,nullable=False)
    updatedAt=Column(String,nullable=False)