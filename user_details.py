import fastapi as _fastapi
import sqlalchemy as _sql
import sqlalchemy.orm as _orm
import sqlalchemy.orm.session

import models.user
from models.user import User
import config

app = _fastapi.FastAPI()

engine = _sql.create_engine(config.DATABASE_URL)
SessionLocal = _orm.sessionmaker(autocommit=False,
                                 autoflush=False,
                                 bind=engine)


def get_user_details(db: sqlalchemy.orm.Session = SessionLocal(), email: str = "") -> dict:
    try:
        user: User | None = db.query(User).filter(User.email == email).first()
        db.close()

        if user is None:
            return {
                'status Code': 404,
                'response': 'user not found'
            }

        return {
            'header': {
                'satus code': 200
            },
            'response': {
                "id": user.id,
                "name": user.name,
                "referral_id": user.referral_id
            }
        }
    except Exception as e:
        print(e)
        raise _fastapi.HTTPException(status_code=500,
                                     detail=f"Internal server error \n {e}") from e


def get_user(db: sqlalchemy.orm.Session = SessionLocal(), email: str = "") -> User | None:
    try:
        user: User | None = db.query(models.user.User).filter(User.email == email).first()
        return user
    except Exception as e:
        print(e)
        raise _fastapi.HTTPException(status_code=500,
                                     detail=f"server error: {e}")


if __name__ == "__main__":
    test_email: str = "abra@gmail.com"
    print(True if get_user(SessionLocal(), email=test_email) else False)
    # print(get_user_details(SessionLocal(), "abra@gmail.com"))
