from sqlalchemy import create_engine, MetaData
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker
import mysql.connector

DATABASE_URL = "mysql+mysqlconnector://root@localhost/tests"

SQL_GET_CURRENT_USER_ID = "SELECT id, name, referral_id, referral_points FROM user WHERE email=%s;"
SQL_GET_REFERED_USER = "SELECT id, email, name, time FROM user WHERE referral_code=%s;"

SECRET_KEY = "83daa0256a2289b0fb23693bf1f6034d44396675749244721a2b20e896e11662"
ALGORITHM = "HS256"
ACCESS_TOKEN_EXPIRE_MINUTES = 30


def get_database():
    mydatabase = mysql.connector.connect(
        host="127.0.0.1",
        user="root",
        password="",
        database="tests",
    )
    if mydatabase:
        return mydatabase
    else:
        print('Cannot connect to database :-(')
        return None


