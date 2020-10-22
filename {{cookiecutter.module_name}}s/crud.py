"""
{{cookiecutter.module_name.title()}} data access object

All CRUD function should be place in here.
"""
from src.db.base_class import CRUDBase
from .orm import {{cookiecutter.module_name.title()}}
from .schemas import {{cookiecutter.module_name.title()}}Create, {{cookiecutter.module_name.title()}}Update


class CRUD{{cookiecutter.module_name.title()}}(CRUDBase[{{cookiecutter.module_name.title()}}, {{cookiecutter.module_name.title()}}Create, {{cookiecutter.module_name.title()}}Update]):
    pass


{{cookiecutter.module_name}} = CRUD{{cookiecutter.module_name.title()}}({{cookiecutter.module_name.title()}})
