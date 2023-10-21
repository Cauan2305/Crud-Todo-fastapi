from app.core.db.mongo_db import Database
from app.core.tasks.entity import TasksDB,TaskUpdate,TaskCreate
from config import credentials
from fastapi import HTTPException
from bson import ObjectId
from datetime import datetime
class TaskService:

    def __init__(self) -> None:
        self.database=Database(credentials['DATABASE_NAME'])

    def create(self,payload:TaskCreate,user_id:str)->TasksDB:
        payload:dict=payload.model_dump()
        payload.update({'creation_date':datetime.now().isoformat(),'last_update':datetime.now().isoformat(),'user_id':user_id})
        self.database.insert("tasks",payload)
        return TasksDB(**payload).model_dump(exclude_none=True)
    
    def update(self,payload:TaskUpdate,user_id:str)->TasksDB:
        payload:dict=payload.model_dump(exclude_none=True)
        payload.update({'last_update':datetime.now().isoformat(),'user_id':user_id})
        document=self.database.update("tasks",{"user_id":user_id},payload)
        document.update(payload)
        return TasksDB(**document).model_dump(exclude_none=True)
    
    def get(self,user_id:str)->TasksDB:
        documents=self.database.find("tasks",{"user_id":user_id},sort=[('priority',1)])
        if not documents:
            raise HTTPException(
                detail="Task Not Found",
                status_code=404
            )
        return [TasksDB(**document).model_dump(exclude_none=True) for document in documents]
