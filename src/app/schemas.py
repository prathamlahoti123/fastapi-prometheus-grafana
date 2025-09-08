from typing import Annotated, TypeAlias

from pydantic import AnyHttpUrl, BaseModel, ConfigDict, EmailStr, Field
from pydantic.alias_generators import to_camel
from pydantic.types import StringConstraints

# type alias to specify a string with constraints
ConstrainedStr: TypeAlias = Annotated[
  str,
  StringConstraints(
    min_length=1,
    max_length=255,
    strip_whitespace=True,
  ),
]


class BaseCustomModel(BaseModel):
  """Base custom pydantic model."""

  model_config = ConfigDict(alias_generator=to_camel, populate_by_name=True)


class Company(BaseCustomModel):
  """Schema representing a company."""

  name: ConstrainedStr
  link: AnyHttpUrl | None = None


class CreateUser(BaseCustomModel):
  """Schema to create a user."""

  first_name: ConstrainedStr
  second_name: ConstrainedStr
  age: Annotated[int, Field(gt=0)]
  email: EmailStr
  country: ConstrainedStr
  job_title: ConstrainedStr
  company: ConstrainedStr


class UpdateUser(BaseCustomModel):
  """Schema to update a user."""

  first_name: ConstrainedStr | None = None
  second_name: ConstrainedStr | None = None
  age: Annotated[int | None, Field(gt=0)] = None
  email: EmailStr | None = None
  country: ConstrainedStr | None = None
  job_title: ConstrainedStr | None = None
  company: ConstrainedStr | None = None
