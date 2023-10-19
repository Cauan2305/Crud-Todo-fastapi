from app.core.users.models import Users,UserCreate
from app.core.db.mongo_db import Database
from app.core.utils.system_hash import SystemHash
from fastapi import HTTPException
class UsersService:

    def __init__(self) -> None:
        self.database=Database("AppTodo")
        self.system_hash=SystemHash()
    def create(self,user:UserCreate)->Users:
        data_duplicated=self.database.find("users",{"email":user.email})   
        if data_duplicated:
            raise HTTPException(detail="This Email Is Already Registered",status_code=400)
        
        password_hashed=self.system_hash.encrypt_password(user.password)
        user.password=password_hashed
        result=self.database.insert("users",user.model_dump())
        user=user.model_dump() 
        del user['password']
        user["id"]=str(result)
        return user