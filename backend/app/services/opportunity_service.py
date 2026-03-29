from repository.opportunity import OpportunityRepository
from models.opportunity import Opportunity, OpportunityCreate
from sqlalchemy.orm import Session
from config.settings import  SEARCH_TERM,LOCATION,RESULTS_WANTED,SITES,OUTPUT_FILE
from scraper.job_scraper import scrape_all_jobs
import pandas as pd
from utils.parser import parse_job,parse_hackathon
from scraper.devpost_scraper import scrape_devpost



class OpportunityService:
    def __init__(self, db: Session):
        self.opportunity_repository = OpportunityRepository(db)

    def create_opportunity(self) -> Opportunity:
        if not SEARCH_TERM or not LOCATION or not RESULTS_WANTED or not SITES:
            raise ValueError("Missing required parameters for job scraping")
        
        job_df = scrape_all_jobs(SEARCH_TERM, LOCATION, RESULTS_WANTED, SITES)
        for _,row in job_df.iterrows():
            opportunity_data = parse_job(row)
            opportunity = self.opportunity_repository.create_opportunity(opportunity_data)

        return opportunity

    def create_hackathon_opportunity(self) -> Opportunity:
        data=scrape_devpost

        for item in data:
            opportunity_data = parse_hackathon(item)
            opportunity = self.opportunity_repository.create_opportunity(opportunity_data)

        return opportunity


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
    
    def isliked(self, opportunity_id: str, user_id: str) -> bool:
        return self.opportunity_repository.isliked(opportunity_id, user_id)
    
  
