from dotenv import load_dotenv
load_dotenv()
from fastapi import FastAPI

from sqlmodel import SQLModel
from modules.routers.tasks_router import router as tasks_router
from modules.routers.users_router import router as users_router
from modules.models.task import Task
from modules.models.user import User

from modules.services.db_services import DbServices

app=FastAPI()

app.include_router(tasks_router)
app.include_router(users_router)
"""
def create_tables():
    lala=DbServices()
    engine=lala.get_engine()
    SQLModel.metadata.create_all(engine)

if __name__ == "__main__":
    create_tables()
"""
