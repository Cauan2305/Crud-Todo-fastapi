from pydantic import BaseModel,EmailStr
class AuthLogin(BaseModel):
    email:EmailStr
    password:str

class AuthResponse(BaseModel):
    Authorization:str