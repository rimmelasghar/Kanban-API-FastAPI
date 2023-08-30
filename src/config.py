import os

# Database settings
DATABASE_URL = os.environ.get("DATABASE_URL") or "postgresql://postgres:03322593149@localhost:5432/mydb"

# App settings
DEBUG = os.environ.get("DEBUG") or True
SECRET_KEY = os.environ.get("SECRET_KEY") or "your_secret_key"
ALGORITHM = "HS256"
ACCESS_TOKEN_EXPIRE_MINUTES = 60 * 24  

DATABASE_USERNAME = "postgres"
DATABASE_PASSWORD = "03322593149"
DATABASE_HOST = "localhost"
DATABASE_NAME = "mydb"


# CORS settings
ALLOWED_ORIGINS = [
    "http://localhost",
    "http://localhost:8000",
    "http://localhost:3000",
]