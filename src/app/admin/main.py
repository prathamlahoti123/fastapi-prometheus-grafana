from typing import TYPE_CHECKING

from sqladmin import Admin

from app.settings import settings

from .views import CompanyAdminView, UserAdminView

if TYPE_CHECKING:
  from fastapi import FastAPI
  from sqlalchemy.ext.asyncio.engine import AsyncEngine


def init_admin_app(app: "FastAPI", db: "AsyncEngine") -> Admin:
  """Init admin app.

  :param app: FastAPI app
  :param db: db engine
  :return: admin app
  """
  admin = Admin(app, db, debug=settings.debug)
  admin.add_view(CompanyAdminView)
  admin.add_view(UserAdminView)
  return admin
