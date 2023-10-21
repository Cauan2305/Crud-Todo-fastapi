from fastapi import APIRouter,status,Depends
from app.core.users.models import UserUpdate,UserCreate,UsersResponseCreate,UsersResponseUpdate
from app.core.users.service import UsersService
from app.routers.validators.validators import validate_token
from fastapi.responses import Response
from datetime import datetime,timedelta

router = APIRouter(prefix="/v1")
service=UsersService()

@router.post("/",response_model=UsersResponseCreate)
async def create(payload:UserCreate,response:Response):
    result,token=service.create(payload)
    expire=(datetime.now()+timedelta(1)).strftime('%a, %d %b %Y %H:%M:%S GMT')
    response.set_cookie(key="Authorization",value=token,expires=expire,path="/")
    response.headers["Authorization"]=f"Bearer {token}"
    response.headers["Expires"]=expire
    return result


@router.put("/",response_model=UsersResponseUpdate,response_model_exclude_none=True)
async def update(payload:UserUpdate,user_id:str=Depends(validate_token)):
    result=service.update(payload,user_id)
    if not result:
        return status.HTTP_304_NOT_MODIFIED
    return result

@router.get("/",response_model=UsersResponseCreate,response_model_exclude_none=True)
async def get(user_id:str=Depends(validate_token)):
    result=service.get(user_id)
    return result


@router.delete("/",status_code=status.HTTP_204_NO_CONTENT)
async def get(user_id:str=Depends(validate_token)):
    service.delete(user_id)