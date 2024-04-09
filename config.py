import hashlib

HOST= "172.24.0.2" # IP of Docker container
USER = "root"
PASS = "abcd"
DATABASE_NAME = "tests"
DATABASE_URL = f"mysql+mysqlconnector://{USER}:{PASS}@{HOST}/{DATABASE_NAME}"

SECRET_KEY = "83daa0256a2289b0fb23693bf1f6034d44396675749244721a2b20e896e11662"
ALGORITHM = "HS256"
ACCESS_TOKEN_EXPIRE_MINUTES = 30
TOKEN_URL = "token"

REFER_REWARD = 100


def getSHA(password):
    SHA_password = hashlib.sha256(password.encode('utf-8')).hexdigest().upper()
    return SHA_password
