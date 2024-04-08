from fastapi import FastAPI, Form
import fastapi.security as _security
import fastapi as _fastapi
import passlib.context as _passlib
import pydantic as _pydantic
import json as _json
import datetime as _datetime
import jwt



from models.user import User
import models.user
import user_registration
import user_details
import refers
import models 
import config


app = FastAPI()

oauth2_scheme = _security.OAuth2PasswordBearer(tokenUrl="token")
pwd_context = _passlib.CryptContext(schemes=["bcrypt"])


class User(_pydantic.BaseModel):
    email : str
    password : str

def get_pass_hash(password):
    return pwd_context.hash(password)

@app.get("/")
def home(token : str = _fastapi.Depends(oauth2_scheme)):
    if check_valid_token(token=token):
        return  {"response": "valid"}
    else:
        return {"response":"valid"}
    
def check_valid_token(token):
    try:
        payload = jwt.decode(token, config.SECRET_KEY, algorithms=config.ALGORITHM)
        expiration_time = _datetime.datetime.utcfromtimestamp(payload["exp"])
        return expiration_time > _datetime.datetime.utcnow()
    except jwt.ExpiredSignatureError:
        return False
    except jwt.InvalidTokenError:
        return False
    
def user_auth(email: str, password : str): 
    user = user_details.get_user(email)
    if not user:
        return False
    if not pwd_context.verify(password, user.password):
        return False
    return user


def create_access_token(data : dict, expires_delta : _datetime.timedelta):
    to_encode = data.copy()
    expire = _datetime.datetime.utcnow() + expires_delta
    to_encode.update({"exp": expire})
    print(to_encode)
    encoded_JWT = jwt.encode(to_encode, config.SECRET_KEY , config.ALGORITHM)
    return encoded_JWT


@app.post("/token")
def login(form_data : _security.OAuth2PasswordRequestForm = _fastapi.Depends()):
    email = form_data.username
    password = form_data.password

    if user_auth(email, password):
        access_token = create_access_token(
            data = {"sub":email}, expires_delta = _datetime.timedelta(minutes=15)
        )
        print(access_token)
        return {"access_token" : access_token, "token_type": "bearer"}
    else:
        raise _fastapi.HTTPException(status_code=400, detail="Incorrect email or password")
 


@app.post("/register/", response_model=dict)
async def register_user(
    name: str = Form(...),
    email: str = Form(...),
    password: str = Form(...),
    referral_code: str = Form(None),
):
    return user_registration.signup(name = name, email= email, password= password, referral_code=referral_code )

@app.get("/user/{email}")
async def get_user_details(email: str):
    return user_details.get_user_details(email=email)

@app.get("/get_refer/{email}")
async def get_refers(email: str):
    return refers.get_refer_info(email=email)


if __name__ == "__main__":
    # user_auth("admin@gmail.com", "Admin1234")
    import uvicorn
    uvicorn.run(app, host="127.0.0.1", port=8000)
