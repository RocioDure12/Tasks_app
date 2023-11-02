from ..repositories.users_repository import UsersRepository
from ..models.user import User

class UsersController():
    def __init__(self):
        self._users_repository=UsersRepository()
    
    def create(self, item:User):
        return self._users_repository.create(item)
    
    def read(self):
        return self._users_repository.read()
    
    def update(self, id:int, item:User):
        return self._users_repository.update(id, item)
    
    def delete(self, id:int):
        return self._users_repository.delete(id)
        
        
    
    