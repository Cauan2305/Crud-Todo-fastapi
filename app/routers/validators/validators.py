from app.core.authentication.service import AuthenticationService
from fastapi import Request,HTTPException
from typing import Optional
from bson import ObjectId

def validate_user_id(user_id:str):
    if ObjectId.is_valid(user_id):
        return user_id 
    raise HTTPException(detail="User Id Invalid",status_code=400)


def validate_token(request:Request)->Optional[dict]:
    service=AuthenticationService()
    user_id= service.authentication_token(request)
    return validate_user_id(user_id)
