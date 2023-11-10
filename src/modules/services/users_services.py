from passlib.context import CryptContext
from fastapi.security import OAuth2PasswordBearer, OAuth2PasswordRequestForm
from ..services.db_services import DbServices
from sqlmodel import Session,select
from ..repositories import users_repository
from fastapi import HTTPException, status
from ..models.user import User
from datetime import timedelta, datetime
from jose import JWTError, jwt
import os
from ..models.auth_response import AuthResponse
from .password_services import PasswordServices


class UsersServices:
    
    def __init__(self):
        self._oauth2_scheme=OAuth2PasswordBearer(tokenUrl="token")
        self._db_services=DbServices()
        self._users_repository= users_repository.UsersRepository()
        self._password_services=PasswordServices()
   
    
    def authenticate_user(self, username:str, plain_password:str):
        user=self._users_repository.read_by_username(username)
        if user is not None and self._password_services.verify_password(plain_password,user.password):
                return user
        
        return None
    
    def handle_authentication(self, username:str, plain_password:str):
        user=self.authenticate_user(username, plain_password)
        if not user:
            raise HTTPException(
            status_code=status.HTTP_401_UNAUTHORIZED,
            detail="Incorrect username or password",
            headers={"WWW-Authenticate": "Bearer"},)
        
        access_token=self.create_access_token(user, [],)
        refresh_token=self.create_refresh_token(user)
        
        return AuthResponse(access_token=access_token, refresh_token=refresh_token)
             
        
    def create_token(self,
                     user:User, 
                     scopes:list[str],
                     expiration_minutes:int,
                     token_secret:str,
                     token_algorithm:str):
        expires_delta=timedelta(minutes=int(expiration_minutes))
        expiration_date=datetime.utcnow() + expires_delta
        data_to_encode = {
            "iat":datetime.utcnow(),
            "sub":user.user_name,
            "exp":expiration_date,
            "scopes":scopes
        }
                
        encoded_jwt = jwt.encode(
            data_to_encode,
            token_secret, 
            algorithm=token_algorithm
        )
        return encoded_jwt   
    
    def create_access_token(self, user:User, scopes:list[str]):
        return self.create_token(user,
                                 scopes,
                                 expiration_minutes=os.getenv(f'JWT_ACCESS_TOKEN_EXPIRE_MINUTES'),
                                 token_secret=os.getenv(f'JWT_ACCESS_TOKEN_SECRET'),
                                 token_algorithm=os.getenv(f'JWT_ACCESS_TOKEN_ALGORITHM')
                                )
                                 
    
        
    def create_refresh_token(self, user:User):
        return self.create_token(user,
                                 [],
                                 expiration_minutes=os.getenv(f'JWT_REFRESH_TOKEN_EXPIRE_MINUTES'),
                                 token_secret=os.getenv(f'JWT_REFRESH_TOKEN_SECRET'),
                                 token_algorithm=os.getenv(f'JWT_REFRESH_TOKEN_ALGORITHM')
                                 )
    
    
    
    
    
    