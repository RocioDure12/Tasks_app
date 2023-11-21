from typing import Optional
from sqlmodel import Field,Relationship,SQLModel
from typing import TYPE_CHECKING
if TYPE_CHECKING:
    from ..models.user import User

class Task(SQLModel, table=True):
    id:Optional[int]=Field(default=None, primary_key=True)
    task_name:str
    description:str
    status:bool
    user_id:Optional[int]=Field(default=None, foreign_key="user.id")
    user:Optional["User"]=Relationship(back_populates="tasks")