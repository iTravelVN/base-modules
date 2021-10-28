"""
{{cookiecutter.module_name.title()}} data access object

All CRUD function should be place in here.
"""
from src.db.base_class import CRUDBase
from .orm import {{cookiecutter.module_name_singular.title()}}
from .schemas import {{cookiecutter.module_name_singular.title()}}Create, {{cookiecutter.module_name_singular.title()}}Update


class CRUD{{cookiecutter.module_name_singular.title()}}(CRUDBase[{{cookiecutter.module_name_singular.title()}}, {{cookiecutter.module_name_singular.title()}}Create, {{cookiecutter.module_name_singular.title()}}Update]):
    pass


{{cookiecutter.module_name_singular}} = CRUD{{cookiecutter.module_name_singular.title()}}({{cookiecutter.module_name_singular.title()}})
