import fastapi.security as _security
import fastapi as _fastapi
import passlib.context as _passlib
import datetime as _datetime
import jwt as _jwt

import user_registration
import user_details
import refers
import config
import token

app = _fastapi.FastAPI()

oauth2_scheme = _security.OAuth2PasswordBearer(tokenUrl=config.TOKEN_URL)
pwd_context = _passlib.CryptContext(schemes=["bcrypt"])


def get_pass_hash(password: str) -> str:
    return pwd_context.hash(password)


@app.get("/")
def home(user_token: str = _fastapi.Depends(oauth2_scheme)) -> dict:
    return token.check_valid_token(token=user_token)


def user_auth(email: str, password: str):
    user = user_details.get_user(email)
    if not user:
        return False
    if not pwd_context.verify(password, user.password):
        return False
    return user


@app.post("/token")
def login(form_data: _security.OAuth2PasswordRequestForm = _fastapi.Depends()):
    email = form_data.username
    password = form_data.password

    if user_auth(email, password):
        access_token = token.access_token(
            payload={"sub": email},
            expires_delta=_datetime.timedelta(minutes=config.ACCESS_TOKEN_EXPIRE_MINUTES)
        )
        return {"access_token": access_token, "token_type": "bearer"}
    else:
        raise _fastapi.HTTPException(status_code=400, detail="Incorrect email or password")


@app.post(path="/register/", response_model=dict)
async def register_user(
        name: str = _fastapi.Form(...),
        email: str = _fastapi.Form(...),
        password: str = _fastapi.Form(...),
        referral_code: str = _fastapi.Form(None),
):
    return user_registration.signup(name=name, email=email, password=password, referral_code=referral_code)


@app.get("/user/{email}", )
async def get_user_details(email: str):
    return user_details.get_user_details(email=email)


@app.get("/get_refer/{email}")
async def get_refers(email: str):
    return refers.get_refer_info(email=email)


if __name__ == "__main__":
    import uvicorn

    uvicorn.run(app, host="127.0.0.1", port=8000)
