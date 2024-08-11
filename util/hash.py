from hashlib import sha256


def hash256(string: str):
    return sha256(string=string.encode("utf-8")).hexdigest().upper()
