from sqlalchemy.orm import Session
from repository.saveopportunity import Save_OpportunityRepository
from models.opportunity import Opportunity, OpportunityCreate


class Save_OpportunityService:
    def __init__(self, db: Session):
        self.save_opportunity_repository = Save_OpportunityRepository(db)


    def save_opportunity(self, opportunity: OpportunityCreate) -> Opportunity:
        return self.save_opportunity_repository.save_opportunity(opportunity)

    def get_all_opportunities(self):
        return self.save_opportunity_repository.get_all_opportunities()
    
    def get_opportunity_by_id(self, opportunity_id: str) -> Opportunity:
        return self.save_opportunity_repository.get_opportunity_by_id(opportunity_id)
    
    def delete_opportunity(self, opportunity_id: str):
        return self.save_opportunity_repository.delete_opportunity(opportunity_id)
    
    def search_opportunities(self, query: str):
        return self.save_opportunity_repository.search_opportunities(query)
    
    def filter_opportunities(self, status: str):
        return self.save_opportunity_repository.filter_opportunities(status)
    
