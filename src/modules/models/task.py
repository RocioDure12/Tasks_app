from typing import Optional
from sqlmodel import Field,Relationship,SQLModel,Column, Date
from sqlalchemy import BigInteger, Integer
from datetime import datetime
from typing import TYPE_CHECKING
if TYPE_CHECKING:
    from ..models.user import User

class Task(SQLModel, table=True):
    id:Optional[int]=Field(default=None, primary_key=True)
    task_name:str
    description:str
    status:bool
    deleted_at:Optional[datetime] = None
    created_at:Optional[datetime] = Field(default_factory=datetime.utcnow,nullable=False)
    updated_at:Optional[datetime] = None
    user_id:Optional[int]=Field(default=None, foreign_key="user.id")
    user:Optional["User"]=Relationship(back_populates="tasks")