from typing import Annotated

from pydantic import EmailStr
from sqlmodel import Field, SQLModel


class CreateCompany(SQLModel):
  """Schema representing a company."""

  name: str = Field(index=True, unique=True)
  link: str | None = None


class UpdateCompany(SQLModel):
  """Schema to update a company."""

  name: str | None = None
  link: str | None = None


class CreateUser(SQLModel):
  """Schema to create a user."""

  first_name: str
  second_name: str
  age: Annotated[int, Field(gt=0)]
  email: EmailStr = Field(unique=True, index=True)
  country: str
  job_title: str
  company_id: str | None = Field(default=None, foreign_key="company.id")


class UpdateUser(SQLModel):
  """Schema to update a user."""

  first_name: str | None = None
  second_name: str | None = None
  age: Annotated[int | None, Field(gt=0)] = None
  email: EmailStr | None = None
  country: str | None = None
  job_title: str | None = None
  company: CreateCompany | None = None
  company_id: str | None = None
