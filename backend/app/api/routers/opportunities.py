from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session
from app.schemas.opportunity import OpportunityCreate
from app.services.opportunity_service import OpportunityService

from core.database import get_db
from typing import List

router=APIRouter(prefix="/opportunities", tags=["Opportunities"])  


@router.post("/", response_model=OpportunityCreate)
def create_opportunity(opportunity: OpportunityCreate, db: Session = Depends(get_db)):
    service = OpportunityService(db)
    return service.create_opportunity(opportunity)

@router.post("/hackathons", response_model=OpportunityCreate)
def create_hackathon_opportunity(db: Session = Depends(get_db)):
    service = OpportunityService(db)
    return service.create_hackathon_opportunity()

@router.get("/", response_model=List[OpportunityCreate])
def get_all_opportunities(db: Session = Depends(get_db)):
    service = OpportunityService(db)
    return service.get_all_opportunities() 

@router.get("/{opportunity_id}", response_model=OpportunityCreate)
def get_opportunity_by_id(opportunity_id: str, db: Session = Depends(get_db)):
    service = OpportunityService(db)
    return service.get_opportunity_by_id(opportunity_id)

@router.get("/search/")
def search_opportunities(query: str, db: Session = Depends(get_db)):
    service = OpportunityService(db)
    return service.search_opportunities(query)

@router.patch("/{opportunity_id}/like")
def like_opportunity(opportunity_id: str, db: Session = Depends(get_db)):
    service = OpportunityService(db)
    return service.like_opportunity(opportunity_id)

@router.delete("/{opportunity_id}")
def delete_opportunities(opportunity_id: str, db: Session = Depends(get_db)):
    service = OpportunityService(db)
    return service.delete_opportunities(opportunity_id)

@router.put("/{opportunity_id}")
def update_opportunity(opportunity_id: str, opportunity: OpportunityCreate, db: Session = Depends(get_db)):
    service = OpportunityService(db)
    return service.update_opportunity(opportunity_id, opportunity)
