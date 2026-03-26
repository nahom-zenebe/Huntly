import uuid
from sqlalchemy.orm import Session
from app.models.opportunity import Opportunity
from app.schemas.opportunity import OpportunityCreate
from fastapi import HTTPException, status



class Save_OpportunityRepository:
    def __init__(self, db: Session):
        self.db = db


    def save_opportunity(self, opportunity: OpportunityCreate) -> Opportunity:
        try:
            if not opportunity:
                raise HTTPException(
                    status_code=status.HTTP_400_BAD_REQUEST,
                    detail="Invalid opportunity data"
                )

            db_opportunity = Opportunity(
                id=str(uuid.uuid4()), 
                **opportunity.model_dump()  
            )

            self.db.add(db_opportunity)
            self.db.commit()
            self.db.refresh(db_opportunity)

            return db_opportunity

        except Exception as e:
            self.db.rollback()
            raise e
        
    def get_all_opportunities(self):
        return self.db.query(Opportunity).all()
    
    def get_opportunity_by_id(self, opportunity_id: str) -> Opportunity:
        try:
            if not opportunity_id:
                raise HTTPException(
                    status_code=status.HTTP_400_BAD_REQUEST,
                    detail="Invalid opportunity ID"
                )

            opportunity = self.db.query(Opportunity).filter(Opportunity.id == opportunity_id).first()

            if not opportunity:
                raise HTTPException(
                    status_code=status.HTTP_404_NOT_FOUND,
                    detail="Opportunity not found"
                )

            return opportunity

        except Exception as e:
            self.db.rollback()
            raise e

        
    def update_opportunity(self, opportunity_id: str, opportunity_data: OpportunityCreate) -> Opportunity:
        try:
            if not opportunity_id or not opportunity_data:
                raise HTTPException(
                    status_code=status.HTTP_400_BAD_REQUEST,
                    detail="Invalid opportunity ID or data"
                )

            opportunity = self.db.query(Opportunity).filter(Opportunity.id == opportunity_id).first()

            if not opportunity:
                raise HTTPException(
                    status_code=status.HTTP_404_NOT_FOUND,
                    detail="Opportunity not found"
                )

            for key, value in opportunity_data.model_dump().items():
                setattr(opportunity, key, value)

            self.db.commit()
            self.db.refresh(opportunity)

            return opportunity

        except Exception as e:
            self.db.rollback()
            raise e
        
    def delete_opportunity(self, opportunity_id: str) -> None:
        try:
            if not opportunity_id:
                raise HTTPException(
                    status_code=status.HTTP_400_BAD_REQUEST,
                    detail="Invalid opportunity ID"
                )

            opportunity = self.db.query(Opportunity).filter(Opportunity.id == opportunity_id).first()

            if not opportunity:
                raise HTTPException(
                    status_code=status.HTTP_404_NOT_FOUND,
                    detail="Opportunity not found"
                )

            self.db.delete(opportunity)
            self.db.commit()

        except Exception as e:
            self.db.rollback()
            raise e
        
    def search_opportunities(self, query: str):
        try:
            if not query:
                raise HTTPException(
                    status_code=status.HTTP_400_BAD_REQUEST,
                    detail="Search query cannot be empty"
                )

            opportunities = self.db.query(Opportunity).filter(
                Opportunity.title.ilike(f"%{query}%") |
                Opportunity.description.ilike(f"%{query}%") |
                Opportunity.location.ilike(f"%{query}%")
            ).all()

            return opportunities

        except Exception as e:
            self.db.rollback()
            raise e
        

    def filter_opportunities(self, type: str = None, location: str = None, isRemote: bool = None):
        try:
            query = self.db.query(Opportunity)

            if type:
                query = query.filter(Opportunity.type == type)
            if location:
                query = query.filter(Opportunity.location.ilike(f"%{location}%"))
            if isRemote is not None:
                query = query.filter(Opportunity.isRemote == str(isRemote))

            return query.all()

        except Exception as e:
            self.db.rollback()
            raise e