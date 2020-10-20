"""
{{cookiecutter.module_name.title()}} Pydantic Schema

Can be use as Request Model and Response Model. MUST follow pydantic specific
and reflect SQLAlchemy ORM
"""
from pydantic import BaseModel, validator
from pydantic_sqlalchemy import sqlalchemy_to_pydantic

from .models.orm import {{cookiecutter.module_name.title()}}


{{cookiecutter.module_name.title()}}Create = sqlalchemy_to_pydantic({{cookiecutter.module_name.title()}})
{{cookiecutter.module_name.title()}}Update = sqlalchemy_to_pydantic({{cookiecutter.module_name.title()}})
