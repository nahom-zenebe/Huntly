import enum
from sqlalchemy import Column, Integer, String, Enum, Array
from sqlalchemy.orm import sessionmaker
from core.database import Base 


class Type(str,enum.Enum):
    JOB="job"
    HACKATHON="hackathon"
    INTERNSHIP="internship"
    SCHOLARSHIP="scholarship"
    


class Opportunity:
    __tablename__ = "opportunities"

    id=Column(Integer,primary_key=True,index=True)
    title=Column(String,index=True,nullable=False)
    definition=Column(String,nullable=False)
    url=Column(String,nullable=False)
    type=Column(Enum(Type),nullable=False,default=Type.JOB)

    postedAt=Column(String,nullable=False)
    Deadline=Column(String,nullable=False)

    location=Column(String,nullable=False)
    tags=Column(Array(String),nullable=True)
    skillsRequired=Column(Array(String),nullable=True)
    isRemote=Column(String,nullable=False)

    #AI score calculated
    score=Column(Integer,nullable=True)
    popularity=Column(Integer,nullable=True)

    sourceId=Column(String,nullable=False)
    sourceUrl=Column(String,nullable=False)

    createdAt=Column(String,nullable=False)
    updatedAt=Column(String,nullable=False)
