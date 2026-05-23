from fastapi import FastAPI
from app.routers import router
from app.config.database import engine, Base

app = FastAPI(
    dependencies=[Depends(jwt_filter)]  # aplica el filtro a TODOS los endpoints
)

Base.metadata.create_all(bind=engine)

app.include_router(router.api_router)