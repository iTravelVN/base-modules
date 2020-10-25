"""
{{cookiecutter.module_name.title()}} Pydantic Schema

Can be use as Request Model and Response Model. MUST follow pydantic specific
and reflect SQLAlchemy ORM
"""
from pydantic_sqlalchemy import sqlalchemy_to_pydantic

from . import orm

{{cookiecutter.module_name.title()}}Create = sqlalchemy_to_pydantic(orm.{{cookiecutter.module_name.title()}})
{{cookiecutter.module_name.title()}}Update = sqlalchemy_to_pydantic(orm.{{cookiecutter.module_name.title()}})
