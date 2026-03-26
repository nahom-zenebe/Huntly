from pydantic import BaseModel


class SaveOpportunityBase(BaseModel):
    userId: int
    opportunityId: int


class SaveOpportunityCreate(SaveOpportunityBase):
    pass


class SaveOpportunityResponse(SaveOpportunityBase):
    id: int
    createdAt: str
    updatedAt: str

    class Config:
        orm_mode = True
