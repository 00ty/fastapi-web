from fastapi import APIRouter

from . import access
from . import users


api_router = APIRouter()
api_router.include_router(access.router, tags=['后台'], prefix='/api/access')
api_router.include_router(users.router, tags=['用户'], prefix='/api/users')