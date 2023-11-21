from typing import Optional, List
from sqlmodel import Field,Relationship, SQLModel
from pydantic import EmailStr
from typing import TYPE_CHECKING
if TYPE_CHECKING:
    from ..models.task import Task



class User(SQLModel, table=True):
    id:Optional[int]=Field(default=None, primary_key=True)
    name:str
    surname:str
    email:EmailStr
    user_name:str
    password:str
    
    tasks: List["Task"]=Relationship(back_populates="user")
    
