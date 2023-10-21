from pydantic import BaseModel,Field,ConfigDict
from typing import Literal,Optional
from bson import ObjectId

class TasksRequest(BaseModel):
    title:str
    description:str
    status:Literal['done','new','deleted','overdue']
    priority:Literal['high','tiny','medium']

class TasksResponse(BaseModel):
    title:Optional[str]=None
    description:Optional[str]=None
    status:Optional[Literal['done','new','deleted','overdue']]=None
    priority:Optional[Literal['high','tiny','medium']]=None
    

class TasksRequestUpdate(BaseModel):
    title:Optional[str]=None
    description:Optional[str]=None
    status:Optional[Literal['done','new','deleted','overdue']]=None
    priority:Optional[Literal['high','tiny','medium']]=None
