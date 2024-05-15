from .api import {{cookiecutter.module_name_plural}}

routers = [
    {"router": {{cookiecutter.module_name_plural}}.router, "prefix": "/{{cookiecutter.module_name_plural}}", "tags": ["{{cookiecutter.module_name_plural}}"]},
]
