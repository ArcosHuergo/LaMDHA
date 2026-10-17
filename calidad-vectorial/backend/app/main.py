from fastapi import Depends, FastAPI
from fastapi.middleware.cors import CORSMiddleware

from app.config.security.jwt_filter import JwtAuthFilter
from app.config.settings import settings
from app.routers import router

app = FastAPI(dependencies=[Depends(JwtAuthFilter())])

origins = [
    "http://localhost:5173",
    settings.frontend_url,
]

app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

app.include_router(router.api_router)