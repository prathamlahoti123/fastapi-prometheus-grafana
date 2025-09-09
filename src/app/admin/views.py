from collections.abc import Sequence
from typing import TYPE_CHECKING, ClassVar

from sqladmin import ModelView

from app.models import User

if TYPE_CHECKING:
  from sqladmin._types import MODEL_ATTR


class UserAdminView(ModelView, model=User):
  """Admin view for the User model."""

  form_columns: ClassVar[Sequence["MODEL_ATTR"]] = [
    "first_name",
    "second_name",
    "age",
    "email",
    "country",
    "city",
    "profession",
  ]
  column_list: ClassVar[str | Sequence["MODEL_ATTR"]] = [
    "first_name",
    "second_name",
    "age",
    "email",
    "country",
    "city",
    "profession",
    "created_at",
  ]
  column_searchable_list: ClassVar[Sequence["MODEL_ATTR"]] = [
    "first_name",
    "second_name",
    "email",
  ]
  column_sortable_list: ClassVar[Sequence["MODEL_ATTR"]] = [
    "age",
    "country",
    "city",
    "profession",
    "created_at",
    "updated_at",
  ]
