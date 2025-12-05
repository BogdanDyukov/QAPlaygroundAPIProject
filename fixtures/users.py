import pytest

from clients.common.schemas.base_schema import BaseSchema
from clients.users.schema import CreateUserRequestSchema, CreateUserResponseSchema
from clients.users.users_client import UsersClient, get_users_client


@pytest.fixture
def users_client() -> UsersClient:
    return get_users_client()


class CreatedUserContext(BaseSchema):
    user_payload: CreateUserRequestSchema
    created_user: CreateUserResponseSchema


@pytest.fixture
def created_user_context(users_client: UsersClient) -> CreatedUserContext:
    user_payload = CreateUserRequestSchema()
    create_user_response = users_client.create_user_api(user_payload)
    created_user = CreateUserResponseSchema.model_validate_json(create_user_response.text)
    return CreatedUserContext(user_payload=user_payload, created_user=created_user)


@pytest.fixture
def created_two_users_contexts(users_client: UsersClient, created_user_context: CreatedUserContext)  -> list[CreatedUserContext]:
    second_user_payload = CreateUserRequestSchema()
    create_second_user_response = users_client.create_user_api(second_user_payload)
    created_second_user = CreateUserResponseSchema.model_validate_json(create_second_user_response.text)
    return [created_user_context, CreatedUserContext(user_payload=second_user_payload, created_user=created_second_user)]
