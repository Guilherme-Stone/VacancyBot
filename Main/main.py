from fastapi import FastAPI
from routes.routes import router
from Config.settings import init_db
from contextlib import asynccontextmanager
from Model.resumeModel import ResumeModel

@asynccontextmanager
async def lifespan(app: FastAPI):
    await init_db()
    yield
app = FastAPI(lifespan=lifespan)
app.include_router(router)




