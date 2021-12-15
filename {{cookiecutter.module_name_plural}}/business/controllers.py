"""
{{cookiecutter.module_name_plural.title()}} controllers

Handle all request to {{cookiecutter.module_name_plural.title()}} resource. MUST follow FastAPI Router.
"""
from fastapi import APIRouter, Depends
from fastapi_utils.cbv import cbv
from sqlalchemy.orm import Session

from src.utils import deps

router = APIRouter()


@cbv(router)
class {{cookiecutter.module_name_singular.title()}}Controller:
    db: Session = Depends(deps.get_db)
