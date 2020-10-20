"""
{{cookiecutter.module_name.title()}} Module

Expose API and Business logic to manage and access {{cookiecutter.module_name.title()}}
resource. MUST be used in `base-fastapi` project template.

Details: https://github.com/tienhm0202/base-fastapi/
"""
from .controllers import router  # noqa

API_PREFIX = "/{{cookiecutter.module_name}}s"
API_TAGS = ["{{cookiecutter.module_name}}s"]
