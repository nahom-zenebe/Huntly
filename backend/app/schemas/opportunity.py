from enum import Enum
from typing import List, Optional

from pydantic import BaseModel


class OpportunityType(str, Enum):
	JOB = "job"
	HACKATHON = "hackathon"
	INTERNSHIP = "internship"
	SCHOLARSHIP = "scholarship"


class OpportunityBase(BaseModel):
	title: str
	definition: str
	url: str
	type: OpportunityType = OpportunityType.JOB
	postedAt: str
	Deadline: str
	location: str
	tags: Optional[List[str]] = None
	skillsRequired: Optional[List[str]] = None
	isRemote: str
	score: Optional[int] = None
	popularity: Optional[int] = None
	sourceId: str
	sourceUrl: str


class OpportunityCreate(OpportunityBase):
	pass


class OpportunityUpdate(BaseModel):
	title: Optional[str] = None
	definition: Optional[str] = None
	url: Optional[str] = None
	type: Optional[OpportunityType] = None
	postedAt: Optional[str] = None
	Deadline: Optional[str] = None
	location: Optional[str] = None
	tags: Optional[List[str]] = None
	skillsRequired: Optional[List[str]] = None
	isRemote: Optional[str] = None
	score: Optional[int] = None
	popularity: Optional[int] = None
	sourceId: Optional[str] = None
	sourceUrl: Optional[str] = None


class OpportunityResponse(OpportunityBase):
	id: int
	createdAt: str
	updatedAt: str

	class Config:
		orm_mode = True
