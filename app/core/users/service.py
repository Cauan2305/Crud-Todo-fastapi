from app.core.users.models import UsersEntity,UserUpdate
from app.core.db.mongo_db import Database
from app.core.utils.system_hash import SystemHash
from config import credentials
from fastapi import HTTPException
from bson import ObjectId
from datetime import datetime
from app.core.authentication.token_service import Token
class UsersService:

    def __init__(self) -> None:
        self.database=Database(credentials['DATABASE_NAME'])
        self.system_hash=SystemHash()

    def create(self,user:UsersEntity)->UsersEntity:
        data_duplicated=self.database.find("users",{"email":user.email,"status":{"$nin":['deleted']}})   
        if data_duplicated:
            raise HTTPException(detail="This Email Is Already Registered",status_code=400)
        __password=user.password
        user.password=self.system_hash.encrypt_password(user.password)
        user=user.model_dump(exclude_none=True)
        user['creation_date']=datetime.now().isoformat()
        user['status']="enabled"
        result=self.database.insert("users",user)
        user["id"]=str(result)
        user['password']=__password
        token=Token().generate_token_session(user)
        return UsersEntity(**user).model_dump(exclude_none=True),token
    
    def update(self,user:UserUpdate,user_id:str)->UserUpdate:
        if user.password:
            password_hashed=self.system_hash.encrypt_password(user.password)
            user.password=password_hashed
        
        self.database.update("users",{"_id":ObjectId(user_id),"status":{"$nin":["deleted"]}},user.model_dump(exclude_none=True))
        user=user.model_dump(exclude_none=True)
        user['last_time_updated']=datetime.now().isoformat()
        return UserUpdate(**user).model_dump(exclude_none=True)
    
    def get(self,user_id:str)->UsersEntity:
        result=self.database.find("users",{"_id":ObjectId(user_id),"status":{"$nin":["deleted"]}})
        if not result:
            raise HTTPException(status_code=404,detail="User Id Not Found")
        return [UsersEntity(**document).model_dump(exclude={'password'},exclude_none=True) for document in result if document][0]
    
    def delete(self,user_id:str)->bool:
        self.database.update("users",{"_id":ObjectId(user_id),"status":{"$nin":["deleted"]}},{"status":"deleted"})
    def _get_by_email_(self,email:str)->UsersEntity:
        document=self.database.find("users",{"email":email,"status":{"$nin":["deleted"]}})
        if not document:
            raise HTTPException(status_code=404,detail="User Id Not Found")
        return UsersEntity(**document[0]).model_dump(exclude_none=True)