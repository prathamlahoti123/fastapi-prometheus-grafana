from typing import TYPE_CHECKING

import pytest
from fastapi import status

if TYPE_CHECKING:
  from httpx import AsyncClient

pytestmark = pytest.mark.anyio


async def test_health(client: "AsyncClient") -> None:
  resp = await client.get("/health")
  assert resp.status_code == status.HTTP_204_NO_CONTENT
  assert resp.headers["x-status"] == "ok"


async def test_admin_home(client: "AsyncClient") -> None:
  resp = await client.get("/admin/")
  assert resp.status_code == status.HTTP_200_OK
  assert '<span class="nav-link-title">Users</span>' in resp.text


async def test_admin_users_index(client: "AsyncClient") -> None:
  resp = await client.get("/admin/user/list")
  assert resp.status_code == status.HTTP_200_OK
  assert '<h3 class="card-title">Users</h3>' in resp.text
