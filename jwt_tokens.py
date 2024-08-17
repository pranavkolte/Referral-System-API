import datetime
import datetime as _datetime

import jwt as _jwt

import config


def create_access_token(payload: dict, expires_delta: _datetime.timedelta) -> str:
    expire: datetime.datetime = _datetime.datetime.utcnow() + expires_delta
    payload.update({"exp": expire})
    return __encode(payload=payload, key=config.SECRET_KEY, algorithm=config.ALGORITHM)


def is_valid(token: str) -> dict:
    try:
        __decode(token=token, key=config.SECRET_KEY, algorithm=config.ALGORITHM)
        return {"status": "OK"}
    except _jwt.ExpiredSignatureError:
        return {"status": "EXPIRED_TOKEN"}

    except _jwt.InvalidTokenError:
        return {"status": "INVALID_TOKEN"}


def __encode(payload: dict, key: str, algorithm: str) -> str:
    return _jwt.encode(
        payload=payload, key=config.SECRET_KEY, algorithm=config.ALGORITHM
    )


def __decode(token: str, key: str, algorithm: str) -> dict:
    return _jwt.decode(jwt=token, key=key, algorithms=[algorithm])


if __name__ == "__main__":
    # ----CREATE TOKEN-----------------
    # email: str = "abc@gmail.com"
    # access_token = create_access_token(
    #     payload={"sub": email},
    #     expires_delta=_datetime.timedelta(minutes=config.ACCESS_TOKEN_EXPIRE_MINUTES)
    # )
    # print(access_token)

    # -------VALIDATE TOKEN------
    print(
        is_valid(
            "eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9"
            ".eyJzdWIiOiJhYmNAZ21haWwuY29tIiwiZXhwIjoxNzIwODA1NDAyfQ"
            ".ditAfbEMQlcT9lyfWkFl8ZoeOTWbYwO354FyCgEZRGc"
        )
    )
