from app.core.authentication.service import AuthenticationService
from fastapi import APIRouter
from fastapi.responses import Response
from datetime import datetime,timedelta
from app.core.authentication.models import AuthLogin,AuthResponse
from config import credentials

router = APIRouter(prefix="/v1")
service=AuthenticationService()

@router.post("/login",status_code=200,response_model=AuthResponse)
async def login(payload:AuthLogin,response:Response):
    token=service.login(payload)
    expire=(datetime.now()+timedelta(1)).strftime('%a, %d %b %Y %H:%M:%S GMT')
    response.set_cookie(key="Authorization",value=token,expires=expire,path="/")
    response.headers["Authorization"]=f"Bearer {token}"
    response.headers["Expires"]=expire
    return {"Authorization":f"Bearer {token}"}



@router.get("/logoff")
async def logout(response:Response):
    response.headers.update({"Authorization":""})
    response.delete_cookie('Authorization')
    return {"detail":"sucess"}