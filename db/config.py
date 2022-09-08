from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker

from setting import settings

DATABASE_URL = settings.DATABASE_URI
print(DATABASE_URL)
engine = create_engine(DATABASE_URL, max_overflow=5,encoding='utf8')
SessionLocal = sessionmaker(engine, expire_on_commit=False)

Base = declarative_base()

def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()