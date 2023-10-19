from pydantic import BaseModel,Field,EmailStr
from typing import Optional,Literal

class Users(BaseModel):
    name:str
    email:EmailStr
    password:str

class UserCreate(Users):
    status:str='enabled'
    


class UserUpdate(Users):
    id:str=Field(alias="_id")
    status:Literal['enabled','disabled','deleted']
    # last_time_updated:Optional[str]=None

class UsersResponse(BaseModel):
    name:str
    email:EmailStr
    id:str
