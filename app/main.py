import string
import random
import time
import logging
import os
from fastapi import FastAPI
from starlette.middleware.base import BaseHTTPMiddleware
from starlette.middleware.cors import CORSMiddleware
from app.core.settings import CORS_ORIGINS
from app.api.routers import init_routers
from prometheus_fastapi_instrumentator import Instrumentator
from app.middleware.http_logger import log_requests
from dotenv import load_dotenv


load_dotenv()  # take environment variables from .env.

app = FastAPI()
log = logging.getLogger("uvicorn.errors")

# init metrics
Instrumentator().instrument(app).expose(app)

# middleware
app.add_middleware(BaseHTTPMiddleware, dispatch=log_requests)


@app.on_event("startup")
async def startup():

    log.info(
        f'Server: {os.environ.get("APP_NAME")} Started Listening on port {os.environ.get("PORT")}'
    )


@app.on_event("shutdown")
async def shutdown():
    log.info(f"Server Is Shutting Down")


cors_origins = [i.strip() for i in CORS_ORIGINS.split(",")]

app.add_middleware(
    CORSMiddleware,
    allow_origins=cors_origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

init_routers(app)
