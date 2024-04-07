from fastapi import FastAPI, HTTPException
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker

import config
from models.user import User

import config
from models.user import User

app = FastAPI()

engine = create_engine(config.DATABASE_URL)
SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)

def get_user(email: str):
    db = SessionLocal()
    user = db.query(User).filter(User.email == email).first()
    if not user:
        raise HTTPException(status_code=404, detail="User not found")
    db.close()

    return {
        "id": user.id,
        "name": user.name,
        "referral_id" : user.referral_id,
        "time" : user.time,
    }