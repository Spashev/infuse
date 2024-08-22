import os
from dotenv import load_dotenv
from pydantic_settings import BaseSettings

load_dotenv()


class Settings(BaseSettings):
    DEBUG: bool = os.getenv('DEBUG', 'False')
    ECHO: bool = os.getenv('ECHO', 'False')

    DATABASE_DEV_HOST: str = os.getenv("DATABASE_DEV_HOST")
    DATABASE_PROD_DB: str = os.getenv("DATABASE_PROD_DB")

    UPLOAD_DIRECTORY: str = os.getenv("UPLOAD_DIRECTORY")

    @property
    def get_dev_url(self) -> str:
        return "sqlite:///../" + self.DATABASE_DEV_HOST

    @property
    def get_prod_url(self) -> str:
        return "sqlite:///../" + self.DATABASE_PROD_DB
