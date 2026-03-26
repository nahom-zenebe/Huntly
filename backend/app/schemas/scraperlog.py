from enum import Enum
from typing import Optional

from pydantic import BaseModel


class ScraperStatus(str, Enum):
    PENDING = "pending"
    SUCCESS = "success"
    FAILURE = "failure"
    PARTIAL = "partial"


class ScraperLogBase(BaseModel):
    sourceId: int
    status: ScraperStatus = ScraperStatus.PENDING
    message: Optional[str] = None
    scrapcount: int = 0


class ScraperLogCreate(ScraperLogBase):
    pass


class ScraperLogResponse(ScraperLogBase):
    id: int
    createdAt: str
    updatedAt: str

    class Config:
        orm_mode = True
