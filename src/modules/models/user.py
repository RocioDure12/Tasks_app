from typing import Optional
from sqlmodel import Field, SQLModel
from pydantic import EmailStr


class User(SQLModel, table=True):
    id:Optional[int]=Field(default=None, primary_key=True)
    name:str
    surname:str
    email:EmailStr
    user_name:str
    password:str
    
