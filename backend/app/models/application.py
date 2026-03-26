import enum
from sqlalchemy import Column, Integer, String, Enum, Array
from sqlalchemy.orm import sessionmaker
from core.database import Base 


class Status(str,enum.Enum):
    APPLIED="applied"
    INTERVIEWING="interviewing"
    REJECTED="rejected"
    OFFERED="offered"
    ACCEPTED="accepted"
    WITHDRAWN="withdrawn"


class Application:
    __tablename__ = "applications"

    id=Column(Integer,primary_key=True,index=True)
    userId=Column(Integer,nullable=False)
    opportunityId=Column(Integer,nullable=False)

    notes=Column(String,nullable=True)
    status=Column(Enum(Status),nullable=False,default=Status.APPLIED)
    appliedAt=Column(String,nullable=False)
    updatedAt=Column(String,nullable=False)