

"""
{
  "firstName": "string",
  "lastName": "string",
  "email": "string",
  "password": "string"
}
    -> DB 유저 정보 저장
    {
        "message": " 회원가입 성공 ",
    }
"""
from fastapi import FastAPI
from pydantic import BaseModel
from fastapi.middleware.cors import CORSMiddleware
app = FastAPI()

# Configure CORS

class UserModel(BaseModel):
    firstName: str
    lastName: str
    email: str
    password: str

@app.post("/signup")
def signup(user:UserModel):
    print("DB에 저장 중....")
    return {"message": "회원가입 성공"}