

import enum
from sqlalchemy import Column, Integer, String, Enum, Array
from sqlalchemy.orm import sessionmaker
from core.database import Base 



class UserPreference:   
    __tablename__ = "userpreferences"

    id=Column(Integer,primary_key=True,index=True)
    userId=Column(String, unique=True, index=True)
    preferredLocations=Column(Array(String))
    preferredRoles=Column(Array(String))
    preferredSkills=Column(Array(String))
    createdAt=Column(String,nullable=False)
    updatedAt=Column(String,nullable=False)
