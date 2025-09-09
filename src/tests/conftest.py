from collections.abc import AsyncIterator

import pytest
from httpx import ASGITransport, AsyncClient
from sqlalchemy.ext.asyncio import (
  AsyncSession,
  async_sessionmaker,
  create_async_engine,
)

from app.dependencies import get_db_session
from app.main import app
from app.models import Base
from app.settings import settings

engine = create_async_engine(settings.test_database_url)
async_session = async_sessionmaker(
  engine,
  class_=AsyncSession,
  expire_on_commit=False,
)


@pytest.fixture(scope="session")
def anyio_backend() -> str:
  """Backend (asyncio) for pytest to run async tests."""
  return "asyncio"


@pytest.fixture(scope="session", autouse=True)
async def migrate_db() -> AsyncIterator[None]:
  """Create and drop test test db on startup and shutdown."""
  async with engine.begin() as conn:
    await conn.run_sync(Base.metadata.create_all)
  yield
  async with engine.begin() as conn:
    await conn.run_sync(Base.metadata.drop_all)


async def override_get_db_session() -> AsyncIterator[AsyncSession]:
  """Override dependency for API routes to interact with db."""
  async with async_session() as session:
    yield session


@pytest.fixture(scope="session")
async def client() -> AsyncIterator[AsyncClient]:
  """Async HTTP client to test FastAPI endpoints."""
  app.dependency_overrides[get_db_session] = override_get_db_session
  transport = ASGITransport(app)
  async with AsyncClient(base_url="http://test", transport=transport) as ac:
    yield ac
