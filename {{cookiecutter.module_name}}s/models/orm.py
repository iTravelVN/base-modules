"""
{{cookiecutter.module_name.title()}} ORM

Use to generate and maintain database migration. Reflect table structure in
database. This is ORM following SQLAlchemy policy. All ORM MUST extends
`zogapp.db.base_class.Base`.
"""
from sqlalchemy import Column, String

from zogapp.db.base_class import Base
from zogapp.utils import get_secret


class Component(Base):
    __tablename__ = "{{cookiecutter.module_name}}s"
