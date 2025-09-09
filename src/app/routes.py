from fastcrud import crud_router

from app.dependencies import get_db_session
from app.models import Company, User
from app.schemas import CreateCompany, CreateUser, UpdateCompany, UpdateUser

# API router to manage users
user_router = crud_router(
  session=get_db_session,
  model=User,
  create_schema=CreateUser,
  update_schema=UpdateUser,
  path="/users",
  tags=["users"],
)

# API router to manage companies
company_router = crud_router(
  session=get_db_session,
  model=Company,
  create_schema=CreateCompany,
  update_schema=UpdateCompany,
  path="/company",
  tags=["companies"],
)
