from fastapi import APIRouter,status,Depends
from app.routers.validators.validators import validate_token
from app.core.tasks.service import TaskService
from app.routers.v1.schemas.tasks import TasksRequest,TasksResponse,TasksRequestUpdate
from typing import Literal
router = APIRouter(prefix="/v1")
service=TaskService()

@router.post("/",response_model=TasksResponse)
async def create(payload:TasksRequest,user_id:str=Depends(validate_token)):
    return service.create(payload,user_id)

@router.put("/",response_model=TasksResponse,response_model_exclude_none=True)
async def update(payload:TasksRequestUpdate,user_id:str=Depends(validate_token)):
    return service.update(payload,user_id)

@router.get("/",response_model=list[TasksResponse],response_model_exclude_none=True)
async def update(sort:int=Literal[1,-1],user_id:str=Depends(validate_token)):
    return service.get(user_id,sort)
