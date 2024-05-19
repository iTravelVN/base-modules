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
    description="Create",
    status_code=status.HTTP_201_CREATED,
)
async def new(
    create_data: {{cookiecutter.module_name_singular.title()}}Create,
    session: AsyncSession = Depends(deps.get_session),
) -> {{cookiecutter.module_name_singular.title()}}:
    {{cookiecutter.module_name_singular}} = {{cookiecutter.module_name_singular.title()}}(
        name=create_data.name,
    )
    await db.create(session, {{cookiecutter.module_name_singular}})

    return {{cookiecutter.module_name_singular}}


@router.get(
    "/{{cookiecutter.module_name_singular}}/{{'{'}}{{cookiecutter.module_name_singular}}_id {{'}'}}",
    response_model={{cookiecutter.module_name_singular.title()}}Response,
    description="Get one",
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
    description="Update",
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


@router.put(
    "/{{cookiecutter.module_name_singular}}/{{'{'}}{{cookiecutter.module_name_singular}}_id {{'}'}}/suspend",
    response_model={{cookiecutter.module_name_singular.title()}}Response,
    description = "Suspend",
    status_code = status.HTTP_202_ACCEPTED,
)
async def suspend(
    {{cookiecutter.module_name_singular}}_id: str,
    session: AsyncSession = Depends(deps.get_session),
    current_user=Depends(users_deps.get_current_user),
) -> {{cookiecutter.module_name_singular.title()}}:
    _ = await db.get_by_id(session, {{cookiecutter.module_name_singular.title()}}, {{cookiecutter.module_name_singular}}_id)  # check if existed
    updated = await db.update(
        session,
        {{cookiecutter.module_name_singular.title()}},
        [{{cookiecutter.module_name_singular.title()}}.user_id == current_user.user_id, {{cookiecutter.module_name_singular.title()}}.id == {{cookiecutter.module_name_singular}}_id],
        {"suspended": 1},
    )
    if len(updated) > 1:
        raise ValueError(vars(updated))

    return updated[0]

@router.put(
    "/{{cookiecutter.module_name_singular}}/{{'{'}}{{cookiecutter.module_name_singular}}_id {{'}'}}/unsuspend",
    response_model={{cookiecutter.module_name_singular.title()}}Response,
    description = "Unsuspend",
    status_code = status.HTTP_202_ACCEPTED,
)
async def unsuspend(
    {{cookiecutter.module_name_singular}}_id: str,
    session: AsyncSession = Depends(deps.get_session),
    current_user=Depends(users_deps.get_current_user),
) -> {{cookiecutter.module_name_singular.title()}}:
    _ = await db.get_by_id(session, {{cookiecutter.module_name_singular.title()}}, {{cookiecutter.module_name_singular}}_id)  # check if existed
    updated = await db.update(
        session,
        {{cookiecutter.module_name_singular.title()}},
        [{{cookiecutter.module_name_singular.title()}}.user_id == current_user.user_id, {{cookiecutter.module_name_singular.title()}}.id == {{cookiecutter.module_name_singular}}_id],
        {"suspended": 0},
    )
    if len(updated) > 1:
        raise ValueError(vars(updated))

    return updated[0]
