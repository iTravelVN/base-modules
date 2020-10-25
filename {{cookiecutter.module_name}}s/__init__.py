"""
{{cookiecutter.module_name.title()}} Module

{{cookiecutter.module_description}}

Expose API and Business logic to manage and access {{cookiecutter.module_name.title()}}
resource. SHOULD be used with `base-fastapi` project template.

Details: https://github.com/tienhm0202/base-fastapi/
"""
from .controllers import router  # noqa: F401

API_PREFIX = "/{{cookiecutter.module_name}}s"
API_TAGS = ["{{cookiecutter.module_name}}s"]
