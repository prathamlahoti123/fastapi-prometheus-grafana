import logging
from functools import lru_cache
from typing import TypedDict

from pydantic_settings import BaseSettings


class FastAPIKwargs(TypedDict):
  """Kwargs for FastAPI app."""

  title: str
  description: str
  version: str
  debug: bool


class LoggingKwargs(TypedDict):
  """Kwargs for logger config."""

  level: int
  format: str


class Settings(BaseSettings):
  """API settings."""

  # FastAPI settings
  title: str = "Users Management App"
  description: str = "CRUD Application to Manage Users"
  version: str = "0.0.1"
  debug: bool = True

  # Logging settings
  log_name: str = "app"
  log_level: int = logging.INFO
  log_format: str = "%(levelname)s - %(name)s - %(asctime)s - %(message)s"

  # Database settings
  database_url: str = "sqlite+aiosqlite:///./test.db"
  test_database_url: str = "sqlite+aiosqlite:///:memory:"

  @property
  def fastapi_kwargs(self) -> FastAPIKwargs:
    """Kwargs for FastAPI app."""
    return FastAPIKwargs(
      title=self.title,
      description=self.description,
      version=self.version,
      debug=self.debug,
    )

  @property
  def logging_kwargs(self) -> LoggingKwargs:
    """Kwargs for logger config."""
    return LoggingKwargs(
      level=self.log_level,
      format=self.log_format,
    )


@lru_cache
def get_settings() -> Settings:
  """Return cached project settings."""
  return Settings()


settings = get_settings()
