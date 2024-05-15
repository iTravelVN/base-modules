from app.core.orm.base_response import BaseResponse
from app.modules.users.schemas.responses import UserResponse


class {{cookiecutter.module_name_singular.title()}}Response(BaseResponse):
    name: str
