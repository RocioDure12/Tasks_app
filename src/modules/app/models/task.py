from typing import Optional
from sqlmodel import Field, SQLModel

class Task(SQLModel, table=True):
    id:Optional[int]=Field(default=None, primary_key=True)
    task_name:str
    description:str
    status:bool