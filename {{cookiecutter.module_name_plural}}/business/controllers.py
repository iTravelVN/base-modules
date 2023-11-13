"""
{{cookiecutter.module_name_plural.title()}} controllers

Handle all request to {{cookiecutter.module_name_plural.title()}} resource. MUST follow FastAPI Router.
"""
from fastapi import APIRouter, Depends, HTTPException
from fastapi_utils.cbv import cbv
from sqlalchemy.orm import Session

from src.utils import deps

from ..models import schemas, crud

router = APIRouter()


@cbv(router)
class {{cookiecutter.module_name_singular.title()}}Controller:
    """
    Generate automatically controller, including:
    - Get list of {{cookiecutter.module_name_singular}} at GET "/" - with limit
    and offset as query parameters
    - Get one {{cookiecutter.module_name_singular}} at GET "/{id}" - with id is
    the database ID
    - Update one {{cookiecutter.module_name_singular}} at POST "/{id}"
    - Delete one {{cookiecutter.module_name_singular}} at DELETE "/{id}"
    """
    db: Session = Depends(deps.get_db)

    @router.get("/")
    def get_{{cookiecutter.module_name_plural}}(self, limit: int = 0, offset: int = 50):
        """
        Get a list of {{cookiecutter.module_name_singular}}
        """
        return crud.{{cookiecutter.module_name_singular}}.get_multi(self.db, skip=offset, limit=limit)

    @router.get("/{item_id}")
    def get_{{cookiecutter.module_name_singular}}(self, item_id: str):
        """
        Get one {{cookiecutter.module_name_singular}} by its ID
        """
        return crud.{{cookiecutter.module_name_singular}}.get(self.db, id=item_id)

    @router.post("/")
    def create_{{cookiecutter.module_name_singular}}(self, item: schemas.{{cookiecutter.module_name_singular.title()}}Create):
        """
        Create one new {{cookiecutter.module_name_singular}}
        """
        return crud.{{cookiecutter.module_name_singular}}.create(self.db, obj_in=item)

    @router.patch("/{item_id}")
    def update_{{cookiecutter.module_name_singular}}(self, item_id: str, item: schemas.{{cookiecutter.module_name_singular.title()}}Update):
        """
        Update {{cookiecutter.module_name_singular}} by its ID
        """
        current_item = crud.{{cookiecutter.module_name_singular}}.get(self.db, id=item_id)
        if not current_item:
            raise HTTPException(status_code=404, detail="Item not found")
        return crud.{{cookiecutter.module_name_singular}}.update(
            self.db, db_obj=current_item, obj_in=item)

    @router.delete("/{item_id}")
    def delete_{{cookiecutter.module_name_singular}}(self, item_id: str):
        """
        Delete a {{cookiecutter.module_name_singular}} by its ID
        """
        return crud.{{cookiecutter.module_name_singular}}.remove(self.db, id=item_id)
