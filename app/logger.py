import logging
from typing import TYPE_CHECKING

if TYPE_CHECKING:
  from logging import Logger


def configure_logging() -> "Logger":
  logging.basicConfig(
    level=logging.INFO,
    format="%(levelname)s - %(name)s - %(asctime)s - %(message)s",
  )
  return logging.getLogger(__name__)
