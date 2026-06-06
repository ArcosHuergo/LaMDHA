from fastapi import FastAPI, Depends
from app.routers import router
from app.config.database import engine, Base
from app.config.security.jwt_filter import JwtAuthFilter
from fastapi.middleware.cors import CORSMiddleware

app = FastAPI(
    dependencies=[Depends(JwtAuthFilter())]
)

Base.metadata.create_all(bind=engine)

origins = [
    "http://localhost:5173",
]

app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

app.include_router(router.api_router)