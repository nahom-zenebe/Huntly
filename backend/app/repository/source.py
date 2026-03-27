import uuid
from sqlalchemy.orm import Session
from app.models.opportunity import Opportunity
from app.schemas.source import SourceCreate,SourceResponse,SourceUpdate
from fastapi import HTTPException, status


class SourceRepository:
    def __init__(self,db):
        self.db=db


    def create_source(self,source:SourceCreate) -> SourceResponse:
        try:
            if not source:
                raise HTTPException(
                    status_code=status.HTTP_400_BAD_REQUEST,
                    detail="Invalid source data"
                )

            db_source = SourceResponse(
                id=str(uuid.uuid4()), 
                **source.model_dump()  
            )

            self.db.add(db_source)
            self.db.commit()
            self.db.refresh(db_source)

            return db_source

        except Exception as e:
            self.db.rollback()
            raise e
        
    def get_all_sources(self):
        return self.db.query(SourceResponse).all()
    

    def get_source_by_id(self, source_id: str) -> SourceResponse:
        try:
            if not source_id:
                raise HTTPException(
                    status_code=status.HTTP_400_BAD_REQUEST,
                    detail="Invalid source ID"
                )

            source = self.db.query(SourceResponse).filter(SourceResponse.id == source_id).first()

            if not source:
                raise HTTPException(
                    status_code=status.HTTP_404_NOT_FOUND,
                    detail="Source not found"
                )

            return source

        except Exception as e:
            self.db.rollback()
            raise e
        
    def update_source(self, source_id: str, source_data: SourceUpdate) -> SourceResponse:
        try:
            if not source_id or not source_data:
                raise HTTPException(
                    status_code=status.HTTP_400_BAD_REQUEST,
                    detail="Invalid source ID or data"
                )

            source = self.db.query(SourceResponse).filter(SourceResponse.id == source_id).first()

            if not source:
                raise HTTPException(
                    status_code=status.HTTP_404_NOT_FOUND,
                    detail="Source not found"
                )

            for key, value in source_data.model_dump(exclude_unset=True).items():
                setattr(source, key, value)

            self.db.commit()
            self.db.refresh(source)

            return source

        except Exception as e:
            self.db.rollback()
            raise e
        
    def delete_source(self, source_id: str) -> None:
        try:
            if not source_id:
                raise HTTPException(
                    status_code=status.HTTP_400_BAD_REQUEST,
                    detail="Invalid source ID"
                )

            source = self.db.query(SourceResponse).filter(SourceResponse.id == source_id).first()

            if not source:
                raise HTTPException(
                    status_code=status.HTTP_404_NOT_FOUND,
                    detail="Source not found"
                )

            self.db.delete(source)
            self.db.commit()

        except Exception as e:
            self.db.rollback()
            raise e
        
    def toggleActive(self,source_id):
        try:
            if source_id is None:
                raise HTTPException(
                    status_code=status.HTTP_400_BAD_REQUEST,
                    detail="Invalid source ID"
                )
            
            source=self.db.query(SourceResponse).filter(SourceResponse.id==source_id).first()
            value=source.isActive
            if not source:
                raise HTTPException(
                    status_code=status.HTTP_404_NOT_FOUND,
                    detail="Source not found"
            )    
            if value==True:
                source.isActive=False

            else:
                source.isActive=True


        except Exception as e:
            self.db.rollback()
            raise e