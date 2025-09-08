import logging
from typing import TYPE_CHECKING

from app.settings import settings

if TYPE_CHECKING:
  from logging import Logger


def configure_logging() -> "Logger":
  logging.basicConfig(**settings.logging_kwargs)
  return logging.getLogger(__name__)
