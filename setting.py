import os
import secrets
from typing import List

from pydantic import BaseSettings
from dotenv import dotenv_values

dotenv_config = dotenv_values('.env')

class Settings(BaseSettings):
    BASEDIR = os.path.abspath(os.path.dirname(__file__))
    LOG_PATH = os.path.join(BASEDIR, 'logs')
    BACKEND_CORS_ORIGINS: List = ['*']

    # 数据库账号密码
    DB_HOST = dotenv_config.get('DB_HOST', '127.0.0.1')
    DB_PORT = dotenv_config.get('DB_PORT', 3306)
    DB_USER = dotenv_config.get('DB_USER', 'root')
    DB_PASSWORD = dotenv_config.get('DB_PASSWORD', 'root')
    DB_NAME = dotenv_config.get('DB_NAME', 'f')

    DATABASE_URI = f'mysql+pymysql://{DB_USER}:{DB_PASSWORD}@{DB_HOST}:{DB_PORT}/{DB_NAME}'
    # SQLALCHEMY_DATABASE_URI: str = f'mysql+aiomysql://{DB_USER}:{DB_PASSWORD}@{DB_HOST}:{DB_PORT}/{DB_NAME}'

settings = Settings()