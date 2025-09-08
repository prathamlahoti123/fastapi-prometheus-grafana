import logging
from typing import TYPE_CHECKING

from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from prometheus_fastapi_instrumentator import Instrumentator

if TYPE_CHECKING:
  from logging import Logger


def configure_logging() -> "Logger":
  logging.basicConfig(
    level=logging.INFO,
    format="%(levelname)s - %(name)s - %(asctime)s - %(message)s",
  )
  return logging.getLogger(__name__)


app = FastAPI()
app.add_middleware(
  CORSMiddleware,
  allow_origins=["*"],
  allow_credentials=True,
  allow_methods=["*"],
  allow_headers=["*"],
)
Instrumentator().instrument(app).expose(app)


@app.get("/")
async def index() -> dict[str, str]:
  return {"message": "Hello, World!"}
