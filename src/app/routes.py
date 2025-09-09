from fastcrud import crud_router

from app.dependencies import get_db_session
from app.models import User
from app.schemas import CreateUser, UpdateUser

# API router to manage users
user_router = crud_router(
  session=get_db_session,
  model=User,
  create_schema=CreateUser,
  update_schema=UpdateUser,
  path="/users",
  tags=["users"],
)
