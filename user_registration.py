from sqlalchemy.orm import sessionmaker
from sqlalchemy import create_engine

from models.user import User
import config

import datetime
import hashlib
import secrets


engine = create_engine(config.DATABASE_URL)
SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)


def signup(name : str, email : str, password : str, referral_code : str):
    
    db = SessionLocal()
    try:
        # Create a new user record
        new_user = User(
            id = set_uid(),
            name=name,
            email=email,
            password=password,
            referral_code=referral_code,
            referral_id=secrets.token_urlsafe(6),
        )
        db.add(new_user)
        db.commit()

        
        if referral_code:
            referrer = db.query(User).filter_by(referral_code=referral_code).first()
            if referrer:
                referrer.referral_points += 100  # Adjust points as needed
                db.commit()
                
                
        # tests.tests_responses.save_UID(new_user.id) for test pupose
        return {"UID": new_user.id, "response": "Success"}
    
    except Exception as e:
        db.rollback()
        return {"error": str(e)}
    finally:
        db.close()
    
def set_uid():

    id = f"{datetime.datetime.now()}" # getting time stamp
    return hashlib.sha1(id.encode()).hexdigest()



if __name__ == "__main__":
    print(set_uid())