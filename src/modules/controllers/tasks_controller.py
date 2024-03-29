# El controlador recepciona las solicitudes http y da una respuesta. Es el punto de entrada de la api
# Ej: La función read del contolador llama a la función read del repositorio y devuelve los elementos obtenidos
# Las funciones del controlador son llamadas desde el router
from ..repositories.tasks_repository import TasksRepository
from ..models.task import Task
from typing import List
from ..services.users_services import UsersServices
from fastapi import Security
from typing import Annotated
from ..models.user import User

class TasksController():
    def __init__(self):
        self._tasks_repository=TasksRepository()
        
    def create(self,item:Task, user:Annotated[User,
                                  Security(UsersServices.check_access_token,
                                           scopes=['tasks:create'])]):
        item.user_id=user.id
        self._tasks_repository.create(item)
        
    def read(self):
        return self._tasks_repository.read()
    
    def read_task(self, id:int):
        return self._tasks_repository.read_task(id)
    
    def update(self,id:int, item:Task):
        print("fsdfs")
        return self._tasks_repository.update(id, item)
        
    def delete(self, id:int):
        return self._tasks_repository.delete(id)