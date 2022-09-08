from sqlalchemy.orm import Session

from db.models import Admin

class AdminDao:
    def __init__(self, db_session : Session):
        self.db_session = db_session 
    def get(self, user_id: int):
        return self.db_session.query(Admin).filter(Admin.id == user_id).first()
    def find(self, username: str):
        return self.db_session.query(Admin).filter(Admin.username == username).first()