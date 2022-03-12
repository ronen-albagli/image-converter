from fastapi import APIRouter
from pydantic import BaseModel
import base64
from PIL import Image
from io import BytesIO
import os


async def convertBase64ToPdf(image_read, image_name):
    data = image_read

    path = os.path.dirname(os.path.abspath(__file__)) + image_name + ".pdf"

    im = Image.open(BytesIO(base64.b64decode(data)))

    im1 = im.convert('RGB')
    im1.save(path)
    outout = ''

    with open(path, "rb") as pdf_file:
        outout = base64.b64encode(pdf_file.read())

    os.remove(path)

    return outout
