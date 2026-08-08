from fastapi import FastAPI, Depends
from contextlib import asynccontextmanager
from app.routers import router
from app.config.database import engine, Base, SessionLocal
from app.config.security.jwt_filter import JwtAuthFilter
from fastapi.middleware.cors import CORSMiddleware
from app.db.init_db import init_db

@asynccontextmanager
async def lifespan(app: FastAPI):
    db = SessionLocal()
    try:
        init_db(db)
    finally:
        db.close()
    yield

app = FastAPI(
    dependencies=[Depends(JwtAuthFilter())],
    lifespan=lifespan
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