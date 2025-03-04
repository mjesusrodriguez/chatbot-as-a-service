import os
from dotenv import load_dotenv

load_dotenv()  # Cargar variables del archivo .env

class Config:
    SECRET_KEY = os.getenv("JWT_SECRET_KEY", "")
    JWT_SECRET_KEY = SECRET_KEY