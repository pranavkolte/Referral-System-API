from sqlalchemy import create_engine, MetaData
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker
import mysql.connector
import hashlib

DATABASE_URL = "mysql+mysqlconnector://root@localhost/tests"

SQL_GET_CURRENT_USER_ID = "SELECT id, name, referral_id, referral_points FROM user WHERE email=%s;"
SQL_GET_REFERED_USER = "SELECT id, email, name, time FROM user WHERE referral_code=%s;"
SQL_GET_USERS = "SELECT email, password FROM user;"
SQL_GET_PWD = "SELECT  password FROM user WHERE email=%s;"

SECRET_KEY = "83daa0256a2289b0fb23693bf1f6034d44396675749244721a2b20e896e11662"
ALGORITHM = "HS256"
ACCESS_TOKEN_EXPIRE_MINUTES = 15

def getSHA(password):
    SHA_password = hashlib.sha256(password.encode('utf-8')).hexdigest().upper()
    return SHA_password

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


