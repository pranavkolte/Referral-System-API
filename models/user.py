import sqlalchemy.ext.declarative as _declarative
import sqlalchemy as _sql
import datetime as _datetime

Base = _declarative.declarative_base()


class User(Base):
    __tablename__: str = "user"
    id = _sql.Column(_sql.String, primary_key=True, index=True)
    name = _sql.Column(_sql.String, index=True)
    email = _sql.Column(_sql.String, unique=True, index=True)
    password = _sql.Column(_sql.String)
    referral_code = _sql.Column(_sql.String, nullable=True)
    referral_points = _sql.Column(_sql.Integer, default=0)
    referral_id = _sql.Column(_sql.String, unique=True, index=True)
    time = _sql.Column(_sql.TIMESTAMP, default=_datetime.datetime.now())
