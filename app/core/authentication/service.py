from fastapi import HTTPException
from app.core.db.mongo_db import Database
from app.core.utils.system_hash import SystemHash
from app.core.authentication.models import AuthLogin
from app.core.users.service import UsersService
from app.core.authentication.token_service import Token
from config import credentials
from fastapi.requests import Request
from fastapi import HTTPException
from datetime import datetime

class AuthenticationService:

    def __init__(self) -> None:
        self.database=Database(credentials['DATABASE_NAME'])
        self.system_hash=SystemHash()
        self.user_service=UsersService()
        self.token_service=Token()
    
    def login(self,user:AuthLogin)->dict:
        self.system_hash
        document_user=self.user_service._get_by_email_(user.email)
        if not document_user:
            raise HTTPException(
                detail="User does not exist",
                status_code=403
            )
        self.authentication_password(document_user['password'],user.password)
        token=self.token_service.generate_token_session(document_user)
        return token
    def authentication_password(self,password_hashed:bytes,password:str)->bool:
        check_password=self.system_hash.check_password(password_hashed,password)
        if not check_password:
            raise HTTPException(
                detail="The Password Is Incorrect",
                status_code=401
            )
        return True
    
    def authentication_token(self,request:Request):
        token=request.headers.get("Authorization") or request.cookies.get("Authorization")
        if not token:
            raise  HTTPException(
                detail="Token Not Sent",
                status_code=401
            )
        info_token:dict=self.token_service.decode_token(token)
        if info_token['expires']>datetime.now().isoformat():
            return info_token['user_id']
        else:
            raise  HTTPException(
                detail="The access token expired, Make Login Again",
                status_code=401
            )
        