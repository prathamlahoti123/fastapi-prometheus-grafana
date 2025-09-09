from collections.abc import AsyncIterator
from contextlib import asynccontextmanager

from fastapi import FastAPI, Response, status
from fastapi.exceptions import RequestValidationError
from fastapi.middleware.cors import CORSMiddleware
from fastcrud.exceptions.http_exceptions import DuplicateValueException
from prometheus_fastapi_instrumentator import Instrumentator
from sqlalchemy.exc import IntegrityError, NoResultFound

from app.admin.main import init_admin_app
from app.db import engine
from app.errors import (
  db_integrity_error_handler,
  db_not_found_error_handler,
  unexpected_error_handler,
  validation_error_handler,
)
from app.logger import configure_logging
from app.models import Base
from app.routes import user_router
from app.settings import settings


@asynccontextmanager
async def lifespan(app: FastAPI) -> AsyncIterator[None]:
  """Run database migrations, init admin app and set app state."""
  # Add logger to the application state
  app.state.logger = configure_logging()
  db_engine = getattr(app.state, "engine", engine)
  # Create database tables
  async with db_engine.begin() as conn:
    await conn.run_sync(Base.metadata.create_all)
  # Initialize admin app
  init_admin_app(app, db_engine)
  yield
  await db_engine.dispose()


app = FastAPI(
  **settings.fastapi_kwargs,
  lifespan=lifespan,
  exception_handlers={
    NoResultFound: db_not_found_error_handler,
    IntegrityError: db_integrity_error_handler,
    DuplicateValueException: db_integrity_error_handler,
    RequestValidationError: validation_error_handler,
    Exception: unexpected_error_handler,
  },
)
app.add_middleware(CORSMiddleware, **settings.cors_kwargs)
app.include_router(user_router)

# Prometheus monitoring stuff
Instrumentator().instrument(app).expose(app)


@app.get("/health", status_code=status.HTTP_204_NO_CONTENT)
async def health() -> Response:
  """Health-check endpoint."""
  return Response(
    status_code=status.HTTP_204_NO_CONTENT,
    headers={"x-status": "ok"},
  )
