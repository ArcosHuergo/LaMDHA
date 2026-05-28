from fastapi import FastAPI, Depends
from app.routers import router
from app.config.database import engine, Base
from app.config.security.jwt_filter import JwtAuthFilter

app = FastAPI(
    dependencies=[Depends(JwtAuthFilter())]
)

Base.metadata.create_all(bind=engine)

app.include_router(router.api_router)