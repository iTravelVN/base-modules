from app.core.orm.base_request import BaseRequest


class {{cookiecutter.module_name_singular.title()}}Create(BaseRequest):
    name: str


class {{cookiecutter.module_name_singular.title()}}Update(BaseRequest):
    name: str
