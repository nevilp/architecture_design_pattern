from fastapi import FastAPI
from commands import create_user
from quries import get_users

app = FastAPI()

@app.post("/users")
def create_user_endpoint(username:str):
    create_user(username)
    return {"message":"user created"}

@app.get("/users")
def get_user_endpoint():
    return {"users": get_users()}
