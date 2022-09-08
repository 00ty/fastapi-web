import os

from fastapi import FastAPI, Request, status
from fastapi.encoders import jsonable_encoder
from fastapi.exceptions import RequestValidationError
from fastapi.responses import JSONResponse, FileResponse
from routers import api_router

from utils import bcrypt

app = FastAPI(
    title='WebApi',
    description='WebApi Application Params Test',
    version='0.0.2'
)


@app.middleware("http")
async def add_process_time_header(request: Request, call_next):
  response = await call_next(request)
  # .headers["X-Process-Time"] = '123'
  print(request.url.path)
  if request.url.path == "/api/access/login":
    return response
  # 验证Token
  token = request.headers.get('Token')
  if token == None:
    return JSONResponse(
        content=jsonable_encoder({
            'code' : 400,
            'msg' : 'Error',
            'error' : 'Lost Token'
        }),
    )
  # Token 合法性
  if bcrypt.has_token(token) == False:
    return JSONResponse(
        content=jsonable_encoder({
            'code' : 400,
            'msg' : 'Error',
            'error' : 'Token'
        }),
    )
  return response

# 配置参数中间件
@app.exception_handler(RequestValidationError)
async def validation_exception_handler(request: Request, exc: RequestValidationError):
    return JSONResponse(
        content=jsonable_encoder({
            'code' : 400,
            'msg' : 'Error',
            'error' : exc.errors()
        }),
    )

app.include_router(api_router)

'''
http://127.0.0.1:8000/redoc
http://127.0.0.1:8000/docs
'''

@app.get("/")
async def root():
    # 载入主页
    backend = os.path.dirname(os.path.abspath(__file__))
    return FileResponse(os.path.join(backend, 'public', 'index.html'))