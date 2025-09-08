from collections.abc import AsyncIterator
from contextlib import asynccontextmanager
from typing import TYPE_CHECKING, TypedDict

from fastapi import FastAPI, Response, status
from fastapi.middleware.cors import CORSMiddleware
from prometheus_fastapi_instrumentator import Instrumentator

from app.logger import configure_logging
from app.settings import settings

if TYPE_CHECKING:
  from logging import Logger


class AppState(TypedDict):
  logger: "Logger"


@asynccontextmanager
async def lifespan(_: FastAPI) -> AsyncIterator[AppState]:
  """Setup and teardown of application state."""
  logger = configure_logging()
  yield AppState(logger=logger)


app = FastAPI(
  **settings.fastapi_kwargs,
  lifespan=lifespan,
)
app.add_middleware(
  CORSMiddleware,
  allow_origins=["*"],
  allow_credentials=True,
  allow_methods=["*"],
  allow_headers=["*"],
)
Instrumentator().instrument(app).expose(app)


@app.get("/health", status_code=status.HTTP_204_NO_CONTENT)
async def health() -> Response:
  """Health-check endpoint."""
  return Response(
    status_code=status.HTTP_204_NO_CONTENT,
    headers={"x-status": "ok"},
  )
