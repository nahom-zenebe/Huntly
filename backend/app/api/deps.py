from fastapi import Depends, HTTPException
from fastapi.security import OAuth2PasswordBearer
from sqlalchemy.orm import Session
from core.database import SessionLocal
from app.core.security import decode_token
from app.models.user import User
from core.database import Base, engine,get_dbget_db
oauth2_scheme = OAuth2PasswordBearer(tokenUrl="/auth/login")





def get_current_user(token: str = Depends(oauth2_scheme),
                     db: Session = Depends(get_db)):
    try:
        payload = decode_token(token)
        user_id = payload.get("sub")

        user = db.query(User).filter(User.id == user_id).first()

        if not user:
            raise HTTPException(status_code=401, detail="User not found")

        return user
    except Exception:
        raise HTTPException(status_code=401, detail="Invalid token")
    
def require_role(role: str):
    def role_checker(user=Depends(get_current_user)):
        if user.role != role:
            raise HTTPException(status_code=403, detail="Forbidden")
        return user
    return role_checker