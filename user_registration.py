import sqlalchemy.orm as _orm
import sqlalchemy as _sql
import fastapi as _fastapi
import passlib.context as _passlib

from models.user import User
import config
import datetime as _datetime
import hashlib as _hashlib
import secrets as _secrets
import re as _regex



engine = _sql.create_engine(config.DATABASE_URL)
SessionLocal = _orm.sessionmaker(autocommit=False, autoflush=False, bind=engine)

pwd_context = _passlib.CryptContext(schemes=["bcrypt"])
def get_pass_hash(password):
    return pwd_context.hash(password)

def check_email(email : str):
    regex = r'\b[A-Za-z0-9._%+-]+@[A-Za-z0-9.-]+\.[A-Z|a-z]{2,7}\b'
    if _regex.fullmatch(regex, email):
        return True
    else: 
        raise _fastapi.HTTPException(status_code=400, detail="Invalid email address")

def check_details(name, email, password):
    # name validation
    if not name : raise _fastapi.HTTPException(status_code=400, detail="Invalid email address")
    
    # password validation 
    reg_pwd = r"^(?=.*[a-z])(?=.*[A-Z])(?=.*\d)[A-Za-z\d]{8,}$"
    if not _regex.match(reg_pwd, password): raise _fastapi.HTTPException(status_code=400, detail="Invalid Password")
    
    # email validation
    reg_email = r'\b[A-Za-z0-9._%+-]+@[A-Za-z0-9.-]+\.[A-Z|a-z]{2,7}\b'
    if not  _regex.fullmatch(reg_email, email): raise _fastapi.HTTPException(status_code=400, detail="Invalid email address")


def signup(name : str, email : str, password : str, referral_code : str):
    
    db = SessionLocal()
    try:
        user = db.query(User).filter(User.email == email).first()
        if user:
            raise _fastapi.HTTPException(status_code=422, detail="Email is already registered with us.")
        # Create a new user 
        new_user = User(
            id = set_uid(),
            name=name,
            email=email,
            password=get_pass_hash(password),
            referral_code=referral_code,
            referral_id=_secrets.token_urlsafe(6), # referal ID for new user
        )

        check_details(name, email, password)
        db.add(new_user)
        db.commit()

        # refral points rewards
        if referral_code:
            referrer = db.query(User).filter_by(referral_id=referral_code).first()
            if referrer:
                referrer.referral_points += config.REFER_REWARD
                db.commit()

        return {"user_id": new_user.id, "response": "success"}
    except Exception as e:
        db.rollback()
        return {"error": str(e)}
    finally:
        db.close()
    
def set_uid():
    id = f"{_datetime.datetime.now()}" # getting time stamp
    return _hashlib.sha1(id.encode()).hexdigest()



if __name__ == "__main__":
    signup("Pranav", "kolte@gmail.com", "Asdasd123", "ZnmgRi59")