import uuid
from sqlalchemy.orm import Session
from app.models.opportunity import Opportunity
from app.schemas.opportunity import OpportunityCreate
from fastapi import HTTPException, status

from datetime import datetime, timedelta

class OpportunityRepository:

    def __init__(self, db: Session):
        self.db = db

    def create_opportunity(self, opportunity: OpportunityCreate) -> Opportunity:
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
        
    def isliked(self, opportunity_id: str, user_id: str) -> bool:
        try:
            if not opportunity_id or not user_id:
                raise HTTPException(
                    status_code=status.HTTP_400_BAD_REQUEST,
                    detail="Invalid opportunity ID or user ID"
                )
            opportunity=self.db.query(Opportunity).filter(Opportunity.id == opportunity_id).first()

            if opportunity.isliked==True:
                return False
            else:
                return True
        
        except Exception as e:
            self.db.rollback()
            raise e


    def update_opportunity(self, opportunity_id: str, opportunity_data: OpportunityCreate) -> Opportunity:
        try:
            if not opportunity_id or not opportunity_data:
                raise HTTPException(
                    status_code=status.HTTP_400_BAD_REQUEST,
                    detail="Invalid input data"
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
        
    def get_stats(self):
        soon = datetime.utcnow() + timedelta(days=7)
        total_opportunities = self.db.query(Opportunity).count()
        job_opportunities = self.db.query(Opportunity).filter(Opportunity.status == "job").count()
        hackthon_opportunities = self.db.query(Opportunity).filter(Opportunity.status == "hackathon").count()
        internship_opportunities = self.db.query(Opportunity).filter(Opportunity.status == "internship").count()
        scholarship_opportunities = self.db.query(Opportunity).filter(Opportunity.status == "scholarship").count()
        deadline_soon_opportunities = self.db.query(Opportunity).filter(Opportunity.Deadline  <= soon).count()

        return {"total_opportunities": total_opportunities, "job_opportunities": job_opportunities, "hackthon_opportunities": hackthon_opportunities, "internship_opportunities": internship_opportunities, "scholarship_opportunities": scholarship_opportunities, "deadline_soon_opportunities": deadline_soon_opportunities}
    
    def search_opportunities(self, query: str):
        return self.db.query(Opportunity).filter(Opportunity.title.ilike(f"%{query}%")).all()
    
    def delete_opportunities(self,oppuntunity_id: str):
        try:
            if oppuntunity_id:
                raise HTTPException(
                    status_code=status.HTTP_400_BAD_REQUEST,
                    detail="Invalid opportunity ID"
                )
            Opportunity=self.db.query(Opportunity).filter(Opportunity.id == oppuntunity_id).first()
            
            if not Opportunity:
                raise HTTPException(
                    status_code=status.HTTP_404_NOT_FOUND,
                    detail="Opportunity not found"
                )
            self.db.query(Opportunity).delete()
            self.db.commit()
        except Exception as e:
            self.db.rollback()
            raise e
    

    