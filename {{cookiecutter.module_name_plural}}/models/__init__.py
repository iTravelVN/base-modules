# SQL Alchemy models declaration.
# https://docs.sqlalchemy.org/en/20/orm/quickstart.html#declare-models
# mapped_column syntax from SQLAlchemy 2.0.

# https://alembic.sqlalchemy.org/en/latest/tutorial.html
# Note, it is used by alembic migrations logic, see `alembic/env.py`

# Alembic shortcuts:
# # create migration
# alembic revision --autogenerate -m "migration_name"

# # apply all migrations
# alembic upgrade head
from sqlalchemy import String
from sqlalchemy.orm import Mapped, mapped_column

from app.core.orm.base import AsyncBase


class {{cookiecutter.module_name_singular.title()}}(AsyncBase):
    __tablename__ = "{{cookiecutter.module_name_singular}}"
    name: Mapped[str] = mapped_column(String(255))