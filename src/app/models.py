from datetime import datetime
from uuid import uuid4

from sqlalchemy import func
from sqlmodel import Field, Relationship, SQLModel

from app.schemas import CreateCompany, CreateUser


class Base(SQLModel):
  """Base database model."""

  id: str = Field(
    default_factory=lambda: str(uuid4()),
    min_length=36,
    max_length=36,
    primary_key=True,
  )
  created_at: datetime = Field(default_factory=func.now)
  updated_at: datetime = Field(
    default_factory=func.now,
    sa_column_kwargs={"onupdate": func.now},
  )


class Company(Base, CreateCompany, table=True):
  """Database model to represent a company."""

  users: list["User"] = Relationship(back_populates="company")

  def __str__(self) -> str:
    return self.name


class User(Base, CreateUser, table=True):
  """Database model to represent a user."""

  company: Company | None = Relationship(back_populates="users")

  def __str__(self) -> str:
    return f"{self.first_name} {self.second_name} ({self.email})"
