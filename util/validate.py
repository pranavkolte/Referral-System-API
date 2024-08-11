from models.user import User
from user_details import get_user
from util.hash import hash256


def user_cred(email: str, password: str) -> bool:
    user: User = get_user(email=email)
    return user is not None and hash256(password) == user.password
