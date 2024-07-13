import fastapi as _fastapi
import sqlalchemy as _sql
import sqlalchemy.orm as _orm
import passlib.context as _passlib

import config
from models.user import User
import config

app = _fastapi.FastAPI()

engine = _sql.create_engine(config.DATABASE_URL)
SessionLocal = _orm.sessionmaker(autocommit=False,
                                 autoflush=False,
                                 bind=engine)

pwd_context = _passlib.CryptContext(schemes=["bcrypt"])


def get_user_details(email: str) -> dict:
    db = SessionLocal()
    user = db.query(User).filter(User.email == email).first()
    if not user:
        raise _fastapi.HTTPException(status_code=404,
                                     detail="User not found")
    db.close()

    return {
        "id": user.id,
        "name": user.name,
        "referral_id": user.referral_id,
        "time": user.time,
    }


def get_user(email: str):
    db = SessionLocal()
    user = db.query(User).filter(User.email == email).first()
    if not user:
        raise _fastapi.HTTPException(status_code=404, detail="USer not found")

    return user


if __name__ == "__main__":
    get_user("admin@gmail.com")
