from sqlmodel import Session, SQLModel, select
from ..models.task import Task
from ..services.db_services import DbServices
from typing import List


#crud

class TasksRepository():
    def __init__(self):
        self._db_services=DbServices()
    
    def create(self, item:Task):
        with Session(self._db_services.get_engine()) as session:
            session.add(item)
            session.commit()
            session.refresh(item)
        
        return item
    
    def read(self)->List[Task]:
        with Session(self._db_services.get_engine()) as session:
            statement=select(Task)
            results=session.exec(statement)
            items=results.all()
        return items
    
    def update(self,id:int, update_item:Task):
        with Session(self._db_services.get_engine()) as session:
            statement=select(Task).where(Task.id == id)
            item=session.exec(statement).one()
            item.task_name=update_item.task_name
            item.description=update_item.description
            item.status=update_item.status
            
            session.add(item)
            session.commit()
            session.refresh(item)
        
        return item
    
    def delete(self,id:int):
        with Session(self._db_services.get_engine()) as session:
            statement=select(Task).where(Task.id == id)
            item=session.exec(statement).one()
            
            session.delete(item)
            session.commit()
            
            
            
            
            
            
            
    
        
        
    

