from enum import Enum
from typing import Optional

from pydantic import BaseModel


class ApplicationStatus(str, Enum):
	APPLIED = "applied"
	INTERVIEWING = "interviewing"
	REJECTED = "rejected"
	OFFERED = "offered"
	ACCEPTED = "accepted"
	WITHDRAWN = "withdrawn"


class ApplicationBase(BaseModel):
	userId: int
	opportunityId: int
	notes: Optional[str] = None
	status: ApplicationStatus = ApplicationStatus.APPLIED
	appliedAt: str


class ApplicationCreate(ApplicationBase):
	pass


class ApplicationUpdate(BaseModel):
	notes: Optional[str] = None
	status: Optional[ApplicationStatus] = None


class ApplicationResponse(ApplicationBase):
	id: int
	updatedAt: str

	class Config:
		orm_mode = True
