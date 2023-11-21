from ..repositories.users_repository import UsersRepository
from ..models.user import User
from fastapi.security import  OAuth2PasswordRequestForm
from typing import Annotated
from fastapi import Depends, Security
from ..services.users_services import UsersServices


class UsersController():
    def __init__(self):
        self._users_repository=UsersRepository()
        self._users_services=UsersServices()
    
    def create(self, item:User):
        return self._users_repository.create(item)
    
    def read(self, user:Annotated[User,
                                  Security(UsersServices.check_access_token,
                                           scopes=['users:read'])],
             ):
        return self._users_repository.read()
    
    def read_by_id(self, id:int):
        return self._users_repository.read_user(id)
    
    
    def read_me(self, user:Annotated[User,
                                  Security(UsersServices.check_access_token,
                                           scopes=['users:read_me'])],
                ):
        return user
    
    
    def update(self, id:int, item:User):
        return self._users_repository.update(id, item)
    
    def delete(self, id:int):
        return self._users_repository.delete(id)
    
    def login_user(self,form_data: Annotated[OAuth2PasswordRequestForm, Depends()]):
        return self._users_services.handle_authentication(form_data.username, form_data.password)
        
        
    
    