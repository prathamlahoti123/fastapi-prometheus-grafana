from pydantic import EmailStr
from sqlmodel import Field, SQLModel


class CreateUser(SQLModel):
  """Schema to create a user."""

  first_name: str
  second_name: str
  age: int = Field(gt=0)
  email: EmailStr = Field(unique=True, index=True)
  country: str
  city: str
  profession: str


class UpdateUser(SQLModel):
  """Schema to update a user."""

  first_name: str | None = None
  second_name: str | None = None
  age: int | None = Field(default=None, gt=0)
  email: EmailStr | None = None
  country: str | None = None
  city: str | None = None
  profession: str | None = None
