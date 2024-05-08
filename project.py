import os
from dotenv import load_dotenv
from pydantic_settings import BaseSettings


class Config(BaseSettings):
    load_dotenv()
    user: str = os.getenv("USER")
    access_key: str = os.getenv("ACCESS_KEY")
    bstack_url: str = os.getenv("BSTACK_URL")
    app: str = os.getenv("APP")


config = Config()
