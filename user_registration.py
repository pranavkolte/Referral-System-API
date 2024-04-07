from sqlalchemy.orm import sessionmaker
from sqlalchemy import create_engine

from models.user import User
import config

import datetime
import hashlib


engine = create_engine(config.DATABASE_URL)
SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)



def signup(name : str, email : str, password : str, referral : str):
    
    try:  
        db = SessionLocal()
        # Signup for new useer
        new_user = User(
            id = set_uid(),
            name=name,
            email=email,
            password=password,
            referral = referral  
        )
        db.add(new_user)
        db.commit()
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