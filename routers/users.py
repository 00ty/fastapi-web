from fastapi import APIRouter,Header

router = APIRouter()

@router.post('/list', description='列表')
async def list(token: str = Header(None)):
  uid = token.split('.')[1]
  print(uid)
  return { 'code' : 400, 'msg' : '测试' }