from passlib.context import CryptContext
from fastapi.security import OAuth2PasswordBearer, OAuth2PasswordRequestForm
from ..services.db_services import DbServices
from sqlmodel import Session,select
from ..repositories.users_repository import UsersRepository
from fastapi import HTTPException, status
from ..models.user import User
from datetime import timedelta, datetime
from jose import JWTError, jwt



class UserServices:
    
    def __init__(self):
        self._password_context=CryptContext(schemes=["bcrypt"], deprecated="auto")
        self._oauth2_scheme=OAuth2PasswordBearer(tokenUrl="token")
        self._db_services=DbServices()
        self._users_repository=UsersRepository()
        
    
    def hash_password(self, plain_password):
        return self._password_context.hash(plain_password)
    
    def verify_password(self,plain_password, hashed_password):
        return self._password_context.verify(plain_password,hashed_password)
    
    def authenticate_user(self, username:str, plain_password:str):
        user=self._users_repository.read_by_username(username)
        if user is not None and self.verify_password(plain_password,user.password):
                return user
        
        return None
    
    def handle_authentication(self, username:str, plain_password:str):
        user=self.authenticate_user(username, plain_password)
        if not user:
            raise HTTPException(
            status_code=status.HTTP_401_UNAUTHORIZED,
            detail="Incorrect username or password",
            headers={"WWW-Authenticate": "Bearer"},
        ) 
        
    def create_token(self,
                     user:User, 
                     scopes:list[str],
                     expiration_minutes:int,
                     token_secret:str,
                     token_algorithm:str):
        expires_delta=timedelta(minutes=expiration_minutes)
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
    
    def create_access_token(self):
        pass
    
    def create_refresh_token():
        pass
    
    
    
    
    
    