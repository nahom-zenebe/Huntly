from enum import Enum
from typing import Optional

from pydantic import BaseModel


class SourceType(str, Enum):
    JOB = "job"
    HACKATHON = "hackathon"
    GENERAL = "general"


class SourceBase(BaseModel):
    name: str
    baseUrl: str
    type: SourceType
    isActive: bool = True
    lastScrapedAt: Optional[str] = None


class SourceCreate(SourceBase):
    pass


class SourceUpdate(BaseModel):
    name: Optional[str] = None
    baseUrl: Optional[str] = None
    type: Optional[SourceType] = None
    isActive: Optional[bool] = None
    lastScrapedAt: Optional[str] = None


class SourceResponse(SourceBase):
    id: int
    createdAt: str
    updatedAt: str

    class Config:
        orm_mode = True
