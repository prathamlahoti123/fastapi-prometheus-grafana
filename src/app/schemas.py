from typing import Annotated, TypeAlias

from pydantic import BaseModel, EmailStr, Field
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


class CreateUser(BaseModel):
  """Schema to create a user."""

  first_name: ConstrainedStr
  second_name: ConstrainedStr
  age: Annotated[int, Field(gt=0)]
  email: EmailStr
  country: ConstrainedStr
  city: ConstrainedStr
  address: ConstrainedStr


class UpdateUser(BaseModel):
  """Schema to update a user."""

  first_name: ConstrainedStr | None = None
  second_name: ConstrainedStr | None = None
  age: Annotated[int | None, Field(gt=0)] = None
  email: EmailStr | None = None
  country: ConstrainedStr | None = None
  city: ConstrainedStr | None = None
  address: ConstrainedStr | None = None
