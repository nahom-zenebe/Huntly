import enum
from sqlalchemy import Column, Integer, String, Enum, Boolean, DateTime, Text
from sqlalchemy.sql import func
from core.database import Base


class Type(str, enum.Enum):
    JOB = "job"
    HACKATHON = "hackathon"
    INTERNSHIP = "internship"
    SCHOLARSHIP = "scholarship"


class Opportunity(Base):
    __tablename__ = "opportunities"

    id = Column(Integer, primary_key=True, index=True)

    title = Column(String, nullable=False, index=True)
    description = Column(Text, nullable=False)

    url = Column(String, nullable=False)

    type = Column(Enum(Type), default=Type.JOB, nullable=False)

    posted_at = Column(DateTime, nullable=True)
    deadline = Column(DateTime, nullable=True)

    location = Column(String, nullable=True)
    is_remote = Column(Boolean, default=False)

    # Instead of Array → use comma-separated or JSON (better)
    tags = Column(Text, nullable=True)
    skills_required = Column(Text, nullable=True)

    # AI fields
    score = Column(Integer, nullable=True)
    popularity = Column(Integer, nullable=True)

    # Source tracking
    source_id = Column(String, nullable=True)
    source_url = Column(String, nullable=True)

    is_liked = Column(Boolean, default=False)

    created_at = Column(DateTime, server_default=func.now())
    updated_at = Column(DateTime, onupdate=func.now())