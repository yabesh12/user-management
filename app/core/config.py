import os
from pathlib import Path

class Settings:
    PROJECT_NAME: str = os.getenv("PROJECT_NAME", Path(__file__).resolve().parents[2].name)

settings = Settings()
