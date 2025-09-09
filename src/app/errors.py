from typing import TYPE_CHECKING, cast

from fastapi import Request, status
from fastapi.exceptions import RequestValidationError
from fastapi.responses import JSONResponse
from fastcrud.exceptions.http_exceptions import DuplicateValueException
from sqlalchemy.exc import IntegrityError, NoResultFound

if TYPE_CHECKING:
  from logging import Logger


async def db_not_found_error_handler(
  request: Request,
  e: NoResultFound,
) -> JSONResponse:
  """Database. Not found error handler."""
  logger = cast("Logger", request.app.state.logger)
  logger.info("Database Not Found Error: %s", e)
  client_message = {"error": "User not found"}
  return JSONResponse(client_message, status.HTTP_404_NOT_FOUND)


async def db_integrity_error_handler(
  request: Request,
  e: IntegrityError | DuplicateValueException,
) -> JSONResponse:
  """Database. Integrity error handler."""
  logger = cast("Logger", request.app.state.logger)
  logger.warning("Database Integrity Error: %s", e)
  client_message = {"error": "User already exists"}
  return JSONResponse(client_message, status.HTTP_409_CONFLICT)


async def validation_error_handler(
  _: Request,
  e: RequestValidationError,
) -> JSONResponse:
  """Pydantic validation error handler."""
  error = e.errors()[0]
  field = error["loc"][1]
  error_message = f"{error['msg']}. Field: {field}"
  client_message = {"detail": error_message}
  return JSONResponse(client_message, status.HTTP_422_UNPROCESSABLE_ENTITY)


async def unexpected_error_handler(
  request: Request,
  e: Exception,
) -> JSONResponse:
  """Error handler for all uncaught exceptions."""
  logger = cast("Logger", request.app.state.logger)
  logger.critical("Internal Server Error: %s", e)
  client_message = {"error": "Service is temporarily unavailable"}
  return JSONResponse(client_message, status.HTTP_500_INTERNAL_SERVER_ERROR)
