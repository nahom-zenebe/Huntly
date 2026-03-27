from repository.opportunity import OpportunityRepository
from models.opportunity import Opportunity, OpportunityCreate
from sqlalchemy.orm import Session  



class OpportunityServvice:
    def __init__(self, db: Session):
        self.opportunity_repository = OpportunityRepository(db)

    def create_opportunity(self, opportunity: OpportunityCreate) -> Opportunity:
        return self.opportunity_repository.create_opportunity(opportunity)

    def get_all_opportunities(self):
        return self.opportunity_repository.get_all_opportunities()
    
    def get_opportunity_by_id(self, opportunity_id: str) -> Opportunity:
        return self.opportunity_repository.get_opportunity_by_id(opportunity_id)
    
    def update_opportunity(self, opportunity_id: str, opportunity_data: OpportunityCreate) -> Opportunity:
        return self.opportunity_repository.update_opportunity(opportunity_id, opportunity_data)
    
    def get_stats(self):
        return self.opportunity_repository.get_stats()
    
    def search_opportunities(self, query: str):
        return self.opportunity_repository.search_opportunities(query)
