import json
import httpx
import asyncio
from fastapi import APIRouter
from pydantic import BaseModel

from app.services.convertor import convertBase64ToPdf

convertor_router = APIRouter()


class Router(BaseModel):
    base64: str
    name: str


@convertor_router.post("/image-2-pdf")
async def extract(params: Router):
    results = await convertBase64ToPdf(params.base64, params.name)

    return results
