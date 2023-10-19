from fastapi import APIRouter
from app.core.users.models import UserUpdate,Users,UserCreate,UsersResponse
from app.core.users.service import UsersService

router = APIRouter()
service=UsersService()

@router.post("/create",response_model=UsersResponse)
async def create(payload:UserCreate):
    return service.create(payload)
