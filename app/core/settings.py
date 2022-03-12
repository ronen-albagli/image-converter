"""
Project Settings file
"""
import os
from starlette.datastructures import CommaSeparatedStrings, Secret

default_route_str = "/api"

CORS_ORIGINS = os.getenv("ALLOWED_HOSTS", "*")

SECRET_KEY = Secret(os.getenv(
    "SECRET_KEY",
    "SOME-SECERT")
)
