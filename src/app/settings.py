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


class CORSMiddlewareKwargs(TypedDict):
  """Kwargs for CORSMiddleware config."""

  allow_origins: list[str]
  allow_credentials: bool
  allow_methods: list[str]
  allow_headers: list[str]


class Settings(BaseSettings):
  """API settings."""

  # FastAPI settings
  title: str = "Users Management App"
  description: str = "CRUD Application to Manage Users"
  version: str = "0.0.1"
  debug: bool = True

  # CORS settings
  cors_allow_credentials: bool = True
  cors_allow_headers: list[str] = ["*"]
  cors_allow_origins: list[str] = ["*"]
  cors_allow_methods: list[str] = ["*"]

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

  @property
  def cors_kwargs(self) -> CORSMiddlewareKwargs:
    """Kwargs for CORS middleware."""
    return CORSMiddlewareKwargs(
      allow_origins=self.cors_allow_origins,
      allow_credentials=self.cors_allow_credentials,
      allow_methods=self.cors_allow_methods,
      allow_headers=self.cors_allow_headers,
    )


@lru_cache
def get_settings() -> Settings:
  """Return cached project settings."""
  return Settings()


settings = get_settings()
