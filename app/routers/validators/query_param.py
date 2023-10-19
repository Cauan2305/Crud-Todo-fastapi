from fastapi import HTTPException
from bson import ObjectId

def validate_user_id(user_id:str):
    if ObjectId.is_valid(user_id):
        return user_id 
    raise HTTPException(detail="User Id Invalid",status_code=400)