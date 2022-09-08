from typing import Union

from fastapi import APIRouter,Depends,Query
from fastapi.encoders import jsonable_encoder
from pydantic import BaseModel
from sqlalchemy.orm import Session

from db.dao.admin_dao import AdminDao
from db.config import get_db

import time
from utils import bcrypt

router = APIRouter()

class User(BaseModel):
    username : Union[str, None] = Query(default=None, min_length=5)
    password : Union[str, None] = Query(default=None, min_length=5)

@router.post('/login', description='登录')
async def login(user: User, db: Session = Depends(get_db)):
    json_data = jsonable_encoder(user)
    user_data = AdminDao(db).find(json_data['username'])
    if user_data == None:
        return { 'code' : 400, 'msg' : '登录失败' }
    if bcrypt.verify_password(json_data['password'],user_data.password):
        # 生成token
        token = bcrypt.get_token(
            user_data.username,
            f'{user_data.password}/{time.strftime("%Y-%m-%d %X", time.localtime())}'
        )
        return { 
            'code' : 200, 'msg' : '登录成功',
            'token' : f'{user_data.username}.{user_data.id}.{token}'
        }
    return { 'code' : 400, 'msg' : '登录失败' }