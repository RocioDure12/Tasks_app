from dotenv import load_dotenv
load_dotenv()
from fastapi import FastAPI
from modules.routers.tasks_router import router as tasks_router
from modules.routers.users_router import router as users_router
from modules.services.db_services import DbServices
from sqlmodel import Field, SQLModel, create_engine 

app=FastAPI()
db=DbServices()

app.include_router(tasks_router)
app.include_router(users_router)


"""def create_tables():
    SQLModel.metadata.create_all(db.get_engine()) 

create_tables()
"""