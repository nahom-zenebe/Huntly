from typing import List

from pydantic import BaseModel


class UserPreferenceBase(BaseModel):
    userId: str
    preferredLocations: List[str]
    preferredRoles: List[str]
    preferredSkills: List[str]


class UserPreferenceCreate(UserPreferenceBase):
    pass


class UserPreferenceUpdate(BaseModel):
    preferredLocations: List[str]
    preferredRoles: List[str]
    preferredSkills: List[str]


class UserPreferenceResponse(UserPreferenceBase):
    id: int
    createdAt: str
    updatedAt: str

    class Config:
        orm_mode = True
