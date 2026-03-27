import uuid
from sqlalchemy.orm import Session
from app.models.opportunity import Opportunity
from app.schemas.notification import NotificationCreate,NotificationResponse,NotificationUpdate
from fastapi import HTTPException, status



class NotificationRepository:
    def __init__(self,db):
        self.db=db


    def create_notification(self,notification:NotificationCreate):
        try:
            if not notification:
                raise HTTPException(
                    status_code=status.HTTP_400_BAD_REQUEST,
                    detail="Invalid source data"
                )
            db_notification=NotificationResponse(
                id=str(uuid.uuid4()),
                **notification.model_dump()
            )

            self.db.add(db_notification)
            self.db.commit()
            self.db.refresh(db_notification)
            
            return db_notification

        except  Exception as e:
            self.db.rollback()
            raise e
        
    def get_all_notification(self):
        return self.db.query(NotificationResponse).all()
    
    def get_notication_by_id(self,notificaiton_id:str)->NotificationResponse:
        try:
            if not notificaiton_id:
                raise HTTPException(
                    status_code=status.HTTP_400_BAD_REQUEST,
                    detail="Invalid source ID"
                )
            
            notification=self.db.query(NotificationResponse).filter(NotificationResponse.id==notificaiton_id).first()
            return notification


        except Exception as e:
            self.db.rollback()
            raise e
    
    def delete_notication(self,notificaiton_id:str)->NotificationResponse:
        try:
            if not notificaiton_id:
                raise HTTPException(
                    status_code=status.HTTP_400_BAD_REQUEST,
                    detail="Invalid source ID"
                )
            
            notification=self.db.query(NotificationResponse).filter(NotificationResponse.id==notificaiton_id).first()
            
            self.db.delete(notification)
            self.db.commit()

        except Exception as e:
            self.db.rollback()
            raise e
