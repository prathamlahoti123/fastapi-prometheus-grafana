from collections.abc import Sequence
from typing import TYPE_CHECKING, ClassVar

from sqladmin import ModelView

from app.models import Company, User

if TYPE_CHECKING:
  from sqladmin._types import MODEL_ATTR


class CompanyAdminView(ModelView, model=Company):
  """Admin view for the Company model."""

  name_plural = "Companies"
  form_columns: ClassVar[Sequence["MODEL_ATTR"]] = [
    "name",
    "link",
  ]
  column_list: ClassVar[str | Sequence["MODEL_ATTR"]] = [
    "name",
    "link",
    "created_at",
    "updated_at",
  ]
  column_searchable_list: ClassVar[Sequence["MODEL_ATTR"]] = ["name"]
  column_sortable_list: ClassVar[Sequence["MODEL_ATTR"]] = [
    "name",
    "created_at",
    "updated_at",
  ]


class UserAdminView(ModelView, model=User):
  """Admin view for the User model."""

  form_columns: ClassVar[Sequence["MODEL_ATTR"]] = [
    "first_name",
    "second_name",
    "age",
    "email",
    "country",
    "job_title",
    "company",
  ]
  column_list: ClassVar[str | Sequence["MODEL_ATTR"]] = [
    "first_name",
    "second_name",
    "age",
    "email",
    "country",
    "job_title",
    "company",
    "created_at",
    "updated_at",
  ]
  column_searchable_list: ClassVar[Sequence["MODEL_ATTR"]] = ["email"]
  column_sortable_list: ClassVar[Sequence["MODEL_ATTR"]] = [
    "age",
    "country",
    "created_at",
    "updated_at",
  ]
