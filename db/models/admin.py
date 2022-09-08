from typing import Union, Any

from sqlalchemy import Integer, Column, String

from db.config import Base

class Admin(Base):
    __tablename__ = 'v2_admin'

    id = Column(Integer, primary_key=True)
    username = Column(String(64), unique=True, index=True)
    password = Column(String(255))
    last_login_time = Column(Integer)
