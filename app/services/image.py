import requests
from PIL import Image
from io import BytesIO

def fetch_image(url: str) -> Image:
    response = requests.get(url)
    return Image.open(BytesIO(response.content))

def resize_image(image: Image, width: int, height: int) -> Image:
    return image.resize((width, height))

def save_image(image: Image, path: str, format: str = "JPEG"):
    image.save(path, format=format)
