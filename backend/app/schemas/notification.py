from enum import Enum
from typing import Optional

from pydantic import BaseModel


class NotificationType(str, Enum):
    APPLICATION_UPDATE = "application_update"
    NEW_OPPORTUNITY = "new_opportunity"
    GENERAL = "general"


class NotificationBase(BaseModel):
    userId: int
    title: str
    message: str
    isRead: bool = False
    type: NotificationType = NotificationType.GENERAL


class NotificationCreate(NotificationBase):
    pass


class NotificationUpdate(BaseModel):
    title: Optional[str] = None
    message: Optional[str] = None
    isRead: Optional[bool] = None
    type: Optional[NotificationType] = None


class NotificationResponse(NotificationBase):
    id: int
    createdAt: str
    updatedAt: str

    class Config:
        orm_mode = True
