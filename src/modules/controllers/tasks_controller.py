# El controlador recepciona las solicitudes http y da una respuesta. Es el punto de entrada de la api
# Ej: La función read del contolador llama a la función read del repositorio y devuelve los elementos obtenidos
# Las funciones del controlador son llamadas desde el router
from ..repositories.tasks_repository import TasksRepository
from ..models.task import Task
from typing import List

class TasksController():
    def __init__(self):
        self._tasks_repository=TasksRepository()
        
    def create(self,item:Task):
        print(item)
        self._tasks_repository.create(item)
        
    
    def read(self):
        return self._tasks_repository.read()
    
    def update(self):
        pass
        
    def delete(self):
        pass