
import enum
from sqlalchemy import Column, Integer, String, Enum, Array,Boolean
from sqlalchemy.orm import sessionmaker
from core.database import Base 



class SaveOpportunity:
    __tablename__ = "saveopportunities"

    id=Column(Integer,primary_key=True,index=True)
    userId=Column(Integer,nullable=False)
    opportunityId=Column(Integer,nullable=False)

    createdAt=Column(String,nullable=False)
    updatedAt=Column(String,nullable=False)
