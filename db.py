from motor.motor_asyncio import AsyncIOMotorClient
from pydantic_settings import BaseSettings

class Settings(BaseSettings):
    mongo_uri: str = "mongodb://localhost:27017" 
    database_name: str = "mydatabase"


settings = Settings()

client = AsyncIOMotorClient(settings.mongo_uri)
database = client[settings.database_name]
