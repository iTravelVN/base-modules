from fastapi import APIRouter, Depends, status
from sqlalchemy.ext.asyncio import AsyncSession

from app.core import db
from app.modules import deps
from app.modules.{{cookiecutter.module_name_plural}}.models import {{cookiecutter.module_name_singular.title()}}
from app.modules.{{cookiecutter.module_name_plural}}.schemas.requests import {{cookiecutter.module_name_singular.title()}}Create, {{cookiecutter.module_name_singular.title()}}Update
from app.modules.{{cookiecutter.module_name_plural}}.schemas.responses import {{cookiecutter.module_name_singular.title()}}Response

router = APIRouter()


@router.post(
    "/{{cookiecutter.module_name_singular}}",
    response_model={{cookiecutter.module_name_singular.title()}}Response,
    description="Create new {{cookiecutter.module_name_singular}}",
    status_code=status.HTTP_201_CREATED,
)
async def new(
    create_data: {{cookiecutter.module_name_singular.title()}}Create,
    session: AsyncSession = Depends(deps.get_session),
) -> {{cookiecutter.module_name_singular.title()}}:
    {{cookiecutter.module_name_singular}} = {{cookiecutter.module_name_singular.title()}}(
        user_id=create_data.user_id,
        address=create_data.address,
        brand=create_data.brand,
    )
    await db.create(session, {{cookiecutter.module_name_singular}})
    await {{cookiecutter.module_name_singular}}.awaitable_attrs.user

    return {{cookiecutter.module_name_singular}}


@router.get(
    "/{{cookiecutter.module_name_singular}}/{{'{'}}{{cookiecutter.module_name_singular}}_id {{'}'}}",
    response_model={{cookiecutter.module_name_singular.title()}}Response,
    description="Get {{cookiecutter.module_name_singular}} information",
    status_code=status.HTTP_200_OK,
)
async def get_one(
    {{cookiecutter.module_name_singular}}_id: str,
    session: AsyncSession = Depends(deps.get_session),
) -> {{cookiecutter.module_name_singular.title()}}:
    data = await db.get_by_id(session, {{cookiecutter.module_name_singular.title()}}, {{cookiecutter.module_name_singular}}_id)
    await data.awaitable_attrs.user

    return data


@router.patch(
    "/{{cookiecutter.module_name_singular}}/{{'{'}}{{cookiecutter.module_name_singular}}_id {{'}'}}",
    response_model={{cookiecutter.module_name_singular.title()}}Response,
    description="Update {{cookiecutter.module_name_singular}} information",
    status_code=status.HTTP_202_ACCEPTED,
)
async def update(
    {{cookiecutter.module_name_singular}}_id: str,
    update_data: {{cookiecutter.module_name_singular.title()}}Update,
    session: AsyncSession = Depends(deps.get_session),
) -> {{cookiecutter.module_name_singular.title()}}:
    _ = await db.get_by_id(session, {{cookiecutter.module_name_singular.title()}}, {{cookiecutter.module_name_singular}}_id)  # check if existed
    updated = await db.update(
        session, {{cookiecutter.module_name_singular.title()}}, {{cookiecutter.module_name_singular}}_id, update_data.model_dump(exclude_unset=True)
    )
    await updated.awaitable_attrs.user

    return updated
