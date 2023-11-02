from sqlmodel import Session, SQLModel, select
from ..models.user import User
from ..services.db_services import DbServices
from typing import List

class UsersRepository:
    def __init__(self):
        self._db_services=DbServices()
        
    def create(self, item:User):
        with Session(self._db_services.get_engine()) as session:
            session.add(item)
            session.commit()
            session.refresh(item)
        
        return item
    
    def read(self)->List[User]:
        with Session(self._db_services.get_engine()) as session:
            statement=select(User)
            results=session.exec(statement)
            items=results.all()
        return items
    
    def update(self,id:int, update_item:User):
        with Session(self._db_services.get_engine()) as session:
            statement=select(User).where(User.id == id)
            item=session.exec(statement).one()
            item.name=update_item.name
            item.surname=update_item.surname
            item.email=update_item.email
            item.user_name=update_item.user_name
            item.password=update_item.password
            
            session.add(item)
            session.commit()
            session.refresh(item)
            
        return item
            
    def delete(self, id:int):
        with Session(self._db_services.get_engine()) as session:
            statement=select(User).where(User.id == id)
            item=session.exec(statement).one()
            session.delete(item)
            session.commit()
            
        