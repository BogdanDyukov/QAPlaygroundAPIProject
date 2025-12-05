from http import HTTPStatus
import allure
import pytest
from allure_commons.types import Severity

from clients.common.schemas.errors_schema import ErrorSchema
from clients.users.schema import (
    CreateUserRequestSchema,
    CreateUserResponseSchema,
    GetUserByIdResponseSchema,
    GetAllUsersResponseSchema,
    UpdateUserRequestSchema,
)
from clients.users.users_client import UsersClient
from fixtures.users import CreatedUserContext
from tools.allure.epics import AllureEpic
from tools.allure.features import AllureFeature
from tools.allure.stories import AllureStory
from tools.assertions.base import assert_status_code
from tools.assertions.users import (
    assert_created_user_matches_payload,
    assert_users_equal,
    assert_user_email_already_taken_error,
    assert_user_in_list,
    assert_user_not_found_error,
    assert_user_not_in_list,
)


@pytest.mark.regression
@pytest.mark.users
@allure.epic(AllureEpic.QA_PLAYGROUND)
@allure.feature(AllureFeature.USERS)
class TestUsers:
    @allure.story(AllureStory.CREATE_ENTITY)
    @allure.title("Create user")
    @allure.severity(Severity.CRITICAL)
    def test_create_user(self, users_client: UsersClient):
        user_payload = CreateUserRequestSchema()
        create_user_response = users_client.create_user_api(user_payload)
        created_user = CreateUserResponseSchema.model_validate_json(create_user_response.text)

        assert_status_code(create_user_response.status_code, HTTPStatus.OK)
        assert_created_user_matches_payload(user_payload, created_user)

        get_user_by_id_response = users_client.get_user_by_id_api(created_user.uuid)
        fetched_user = GetUserByIdResponseSchema.model_validate_json(get_user_by_id_response.text)

        assert_status_code(get_user_by_id_response.status_code, HTTPStatus.OK)
        assert_users_equal(fetched_user, created_user)

        get_all_users_response  = users_client.get_all_users_api()
        users_list = GetAllUsersResponseSchema.model_validate_json(get_all_users_response .text)

        assert_status_code(get_all_users_response .status_code, HTTPStatus.OK)
        assert_user_in_list(users_list, created_user)

    @allure.story(AllureStory.DELETE_ENTITY)
    @allure.title("Delete user")
    @allure.severity(Severity.CRITICAL)
    def test_delete_user(self, users_client: UsersClient, created_user_context: CreatedUserContext):
        delete_user_response = users_client.delete_user_api(created_user_context.created_user.uuid)

        assert_status_code(delete_user_response.status_code, HTTPStatus.NO_CONTENT)

        get_user_by_id_response = users_client.get_user_by_id_api(created_user_context.created_user.uuid)
        user_not_found_error = ErrorSchema.model_validate_json(get_user_by_id_response.text)

        assert_status_code(get_user_by_id_response.status_code, HTTPStatus.NOT_FOUND)
        assert_user_not_found_error(user_not_found_error, created_user_context.created_user.uuid)

        get_all_users_response = users_client.get_all_users_api()
        users_list = GetAllUsersResponseSchema.model_validate_json(get_all_users_response.text)

        assert_status_code(get_all_users_response.status_code, HTTPStatus.OK)
        assert_user_not_in_list(users_list, created_user_context.created_user)

    @allure.story(AllureStory.VALIDATE_ENTITY)
    @allure.title("Update user with occupied data")
    @allure.severity(Severity.NORMAL)
    def test_update_user_with_occupied_data(self, users_client: UsersClient, created_two_users_contexts: list[CreatedUserContext]):
        first_user_email = created_two_users_contexts[0].created_user.email
        second_user_uuid = created_two_users_contexts[1].created_user.uuid

        update_payload = UpdateUserRequestSchema(email=first_user_email)
        update_second_user_response = users_client.update_user_api(second_user_uuid, update_payload)
        conflict_error = ErrorSchema.model_validate_json(update_second_user_response.text)

        assert_status_code(update_second_user_response.status_code, HTTPStatus.CONFLICT)
        assert_user_email_already_taken_error(conflict_error, first_user_email)
