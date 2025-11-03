# Settings management
from pydantic_settings import BaseSettings, SettingsConfigDict
from pydantic_core._pydantic_core import ValidationError

from pathlib import Path

from logs import logging
logger = logging.getLogger(__name__)

class Settings(BaseSettings):
    immich_api_key: str
    immich_server: str
    immich_album_name: str
    output_dir: str = str(Path.cwd() / "output")
    model_config = SettingsConfigDict(env_file=".env", cli_parse_args=True) # Load settings from .env file is available, or from CLI args

def get_settings():
    try:
        s = Settings()
    except ValidationError as e:
        logger.error("Settings validation error: %s", e)
        print("Error: Invalid settings. Please check your .env file.")
        exit(1)
    return s
