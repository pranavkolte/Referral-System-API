from fastapi import FastAPI, Form



import user_registration
import user_details
app = FastAPI()

@app.post("/register/", response_model=dict)
async def register_user(
    name: str = Form(...),
    email: str = Form(...),
    password: str = Form(...),
    referral_code: str = Form(None),
):
    return user_registration.signup(name = name, email= email, password= password, referral_code=referral_code )

@app.get("/user/{email}")
def get_user(email: str):
    return user_details.get_user(email=email)

if __name__ == "__main__":
    import uvicorn
    uvicorn.run(app, host="127.0.0.1", port=8000)
