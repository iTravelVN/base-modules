# -*- coding: utf-8 -*-
"""
Define all {{cookiecutter.module_name.title()}} exception.

Exception SHOULD HAVE detail in dict with both english and vietnamese. We did
this app for people, so keep it simple to show message error.

For example:
class InvalidEmail(HTTPException):
    def __init__(self):
        super(InvalidEmail, self).__init__(
            status_code=status.HTTP_400_BAD_REQUEST,
            detail={
                "en": "Email is not valid",
                "vi": "Email không đúng định dạng"
            }
        )
"""
from fastapi import HTTPException
from starlette import status
