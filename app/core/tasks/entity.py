from pydantic import BaseModel,Field,ConfigDict,validator
from typing import Literal
from bson import ObjectId
from typing import Optional

class TaskBase(BaseModel):
    title:str
    description:str
    status:Literal['done','new','deleted','overdue']='new'
    priority:Literal['high','tiny','medium']

class TaskUpdate(BaseModel):
    title:Optional[str]
    description:Optional[str]
    status:Optional[Literal['done','new','deleted','overdue']]
    priority:Optional[Literal['high','tiny','medium']]

class TaskCreate(TaskBase):
    status: Literal['new'] = 'new'

class TasksDB(TaskBase):
    user_id:str
    creation_date:Optional[str]=None
    last_update:str
