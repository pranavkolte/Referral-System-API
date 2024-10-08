import datetime as _datetime

import fastapi as _fastapi
import fastapi.security as _security

import config
import jwt_tokens
import refers
import user_details
import user_registration
from util.validate import user_cred

app = _fastapi.FastAPI()

oauth2_scheme = _security.OAuth2PasswordBearer(tokenUrl=config.TOKEN_URL)


@app.get("/")
def home(user_token: str = _fastapi.Depends(oauth2_scheme)) -> dict:
    return jwt_tokens.is_valid(token=user_token)


@app.post(path="/token")
def login(form_data: _security.OAuth2PasswordRequestForm = _fastapi.Depends()) -> dict:
    email: str = form_data.username
    password: str = form_data.password

    if user_cred(email=email, password=password):
        access_token: str = jwt_tokens.create_access_token(
            payload={"sub": email},
            expires_delta=_datetime.timedelta(
                minutes=config.ACCESS_TOKEN_EXPIRE_MINUTES
            ),
        )
        return {"access_token": access_token, "token_type": "bearer"}
    else:
        raise _fastapi.HTTPException(
            status_code=400, detail="Incorrect email or password"
        )


@app.post(path="/user/", response_model=dict)
async def register_user(
    name: str = _fastapi.Form(...),
    email: str = _fastapi.Form(...),
    password: str = _fastapi.Form(...),
    referral_code: str = _fastapi.Form(None),
) -> dict:
    return user_registration.signup(
        name=name, email=email, password=password, referral_code=referral_code
    )


@app.get(path="/user/{email}")
async def get_user_details(email: str):
    return user_details.get_user_details(email=email)


@app.get("/refer/{email}")
async def get_refers(email: str):
    return refers.get_refer_info(email=email)


if __name__ == "__main__":
    import uvicorn

    uvicorn.run("main:app", host="127.0.0.1", port=8000, reload=True)
