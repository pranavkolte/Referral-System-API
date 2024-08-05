from os import getenv

import fastapi as _fastapi
import sqlalchemy as _sql
import sqlalchemy.orm as _orm
import sqlalchemy.orm.query
from dotenv import load_dotenv

from models.user import User

load_dotenv()

engine = _sql.create_engine(getenv("DATABASE_URL"))
Session = _orm.sessionmaker(autocommit=False, autoflush=False, bind=engine)


def get_user_info(db: _orm.Session, email) -> str:
    """
    This Function takes email and returns User info with referral ID
    :param db: sqlalchemy.orm.Session
    :param email: str
    :return: models.user.User
    """
    try:
        user: User = db.query(User).filter(User.email == email).first()
        if not user:
            raise _fastapi.HTTPException(status_code=404, detail="Not Found")
        return user.referral_id
    finally:
        db.close()


def get_refer_info(email: str) -> dict:
    """
    This Function takes user email and gives referrals of user
    :param email: str
    :return: dict
    """
    # user: User =
    referral_id: str = get_user_info(db=Session(), email=email)
    clauses: list = [User.referral_code == referral_id]
    res: sqlalchemy.orm.query.Query = Session().query(User).filter(_sql.or_(*clauses))
    response: dict = {}
    idx = 0
    for ref_user in res.all():
        idx += 1
        response[idx] = {
            "id": ref_user.id,
            "email": ref_user.email,
            "name": ref_user.name,
            "time": ref_user.time,
        }

    return response


if __name__ == "__main__":
    print(get_refer_info("abra@gmail.com"))
