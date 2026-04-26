from fastapi import FastAPI
from app.routers import router
from app.config.database import engine, Base

app = FastAPI()

Base.metadata.create_all(bind=engine)

app.include_router(router.api_router)