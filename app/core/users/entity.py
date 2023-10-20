from pydantic import BaseModel,Field,EmailStr
from typing import Optional,Literal
from bson import ObjectId

class Users(BaseModel):
    id:ObjectId=Field(alias='_id')
    name:str
    email:EmailStr
    status:Optional[Literal['enabled','disabled','deleted']]='enabled'
    last_time_updated:Optional[str]=None
    creation_date:Optional[str]=None
    class Config:
        arbitrary_types_allowed=True
    