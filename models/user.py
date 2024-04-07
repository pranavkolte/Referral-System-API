from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy import Column,String

Base = declarative_base()

class User(Base):
    __tablename__ = "user"
    id = Column(String, primary_key=True, index=True)
    name = Column(String, index=True)
    email = Column(String, unique=True, index=True)
    password = Column(String)
    referral = Column(String)
    