from fastapi import FastAPI, Form



import user_registration

app = FastAPI()

@app.post("/register/", response_model=dict)
async def register_user(
    name: str = Form(...),
    email: str = Form(...),
    password: str = Form(...),
    referral: str = Form(None),
):
    return user_registration.signup(name, email, password, referral)



if __name__ == "__main__":
    import uvicorn
    uvicorn.run(app, host="127.0.0.1", port=8000)
