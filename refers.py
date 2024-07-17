import sqlalchemy as _sql
import sqlalchemy.orm as _orm
import fastapi as _fastapi

import config
import models.user as _user

engine = _sql.create_engine(config.DATABASE_URL)
Session = _orm.sessionmaker(autocommit=False, autoflush=False, bind=engine)


def get_user_info(email: str):
    db = Session()
    user = db.query(_user.User).filter(_user.User.email == email).first()
    if not user:
        raise _fastapi.HTTPException(status_code=404, detail="Not Found")
    db.close()
    return user


def get_refer_info(email: str):
    user = get_user_info(email=email)
    referral_id = user.referral_id
    clauses = [_user.User.referral_code == referral_id]
    res = Session().query(_user.User).filter(_sql.or_(*clauses))
    # .from_statement(_sql.text(f"SELECT id, email, name, time FROM user WHERE referral_code={referral_id};")).all()
    response = {}
    idx = 0
    for ref_user in res.all():
        idx += 1
        response[idx] = {'id': ref_user.id, 'email': ref_user.email, 'name': ref_user.name, 'time': ref_user.time}

    return response


if __name__ == "__main__":
    print(get_refer_info("nitesh342@gmail.com"))
