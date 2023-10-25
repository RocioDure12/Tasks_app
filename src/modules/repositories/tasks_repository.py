from sqlmodel import Session
from ..models.task import Task
from ..services.db_services import DbServices
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
    
        
        
    

