from dotenv import load_dotenv
load_dotenv()
from fastapi import FastAPI
from modules.routers.tasks_router import router as tasks_router
from modules.routers.users_router import router as users_router

app=FastAPI()

app.include_router(tasks_router)
app.include_router(users_router)


    