from pydantic import BaseModel,Field,EmailStr,ConfigDict,validator
from typing import Optional,Literal
from bson import ObjectId

class UsersEntity(BaseModel):
    id:Optional[ObjectId]=Field(alias='_id')
    name:str
    email:EmailStr
    password:str
    creation_date:Optional[str]=None
    last_time_update:Optional[str]=None
    model_config = ConfigDict(arbitrary_types_allowed=True)


    @validator('id')
    def validate(cls, v):
        if type(v) is ObjectId:
            return str(v)
        return v

    
class UserCreate(BaseModel):
    name:str
    email:EmailStr
    password:str

class UserUpdate(BaseModel):
    status:Optional[Literal['enabled','disabled']]='enabled'
    name:str
    password:Optional[str]=None
    

class UsersResponseCreate(BaseModel):
    name:str
    email:EmailStr
    id:str
    creation_date:Optional[str]=None

class UsersResponseUpdate(BaseModel):
    name:str
    creation_date:Optional[str]=None
    last_time_update:Optional[str]=None
    status:Optional[Literal['enabled','disabled']]=None


    