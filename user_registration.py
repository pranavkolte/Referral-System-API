from sqlalchemy.orm import sessionmaker
from sqlalchemy import create_engine
from fastapi import HTTPException
import passlib.context as _passlib

from models.user import User
import config

import datetime
import hashlib
import secrets
import re

import tests.tests_responses


engine = create_engine(config.DATABASE_URL)
SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)

pwd_context = _passlib.CryptContext(schemes=["bcrypt"])
def get_pass_hash(password):
    return pwd_context.hash(password)

def check_email(email : str):
    regex = r'\b[A-Za-z0-9._%+-]+@[A-Za-z0-9.-]+\.[A-Z|a-z]{2,7}\b'
    if re.fullmatch(regex, email):
        return True
    else: 
        raise HTTPException(status_code=400, detail="Invalid email address")

def check_details(name, email, password):
    if not name : raise HTTPException(status_code=400, detail="Invalid email address")
    
    reg_pwd = r"^(?=.*[a-z])(?=.*[A-Z])(?=.*\d)[A-Za-z\d]{8,}$"
    if not re.match(reg_pwd, password): raise HTTPException(status_code=400, detail="Invalid Password")

    reg_email = r'\b[A-Za-z0-9._%+-]+@[A-Za-z0-9.-]+\.[A-Z|a-z]{2,7}\b'
    if not  re.fullmatch(reg_email, email): raise HTTPException(status_code=400, detail="Invalid email address")


def signup(name : str, email : str, password : str, referral_code : str):
    
    db = SessionLocal()
    try:
        user = db.query(User).filter(User.email == email).first()
        if user:
            raise HTTPException(status_code=422, detail="Email is already registered with us.")
        # Create a new user 
        new_user = User(
            id = set_uid(),
            name=name,
            email=email,
            password=get_pass_hash(password),
            referral_code=referral_code,
            referral_id=secrets.token_urlsafe(6), #generating referal ID for new user
        )

        check_details(name, email, password)
        db.add(new_user)
        db.commit()

        # Award referral points if a valid referral code is provided
        if referral_code:
            referrer = db.query(User).filter_by(referral_id=referral_code).first()
            if referrer:
                referrer.referral_points += 100  # Adjust points as needed
                db.commit()

        return {"user_id": new_user.id, "response": "success"}
    except Exception as e:
        db.rollback()
        return {"error": str(e)}
    finally:
        db.close()
    
def set_uid():

    id = f"{datetime.datetime.now()}" # getting time stamp
    return hashlib.sha1(id.encode()).hexdigest()



if __name__ == "__main__":
    signup("Pranav", "kolte@gmail.com", "Asdasd123", "ZnmgRi59")