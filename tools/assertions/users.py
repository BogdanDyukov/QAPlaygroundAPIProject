import allure
from clients.common.schemas.errors_schema import ErrorSchema
from clients.users.schema import (
    CreateUserRequestSchema,
    CreateUserResponseSchema,
    GetAllUsersResponseSchema,
    UserSchema,
)
from tools.assertions.base import assert_equal, assert_single_match, assert_zero_match
from tools.assertions.errors import assert_error_response


@allure.step("Check created user matches payload")
def assert_created_user_matches_payload(user_payload: CreateUserRequestSchema, created_user: CreateUserResponseSchema):
    assert_equal(user_payload.email, created_user.email, "Email")
    assert_equal(user_payload.name, created_user.name, "Name")
    assert_equal(user_payload.nickname, created_user.nickname, "Nickname")


@allure.step("Check users equal")
def assert_users_equal(first_user: UserSchema, second_user: UserSchema):
    assert_equal(first_user.email, second_user.email, "Email")
    assert_equal(first_user.name, second_user.name, "Name")
    assert_equal(first_user.nickname, second_user.nickname, "Nickname")
    assert_equal(first_user.avatar_url, second_user.avatar_url, "AvatarUrl")
    assert_equal(first_user.uuid, second_user.uuid, "UUID")


@allure.step("Check user in list of users")
def assert_user_in_list(user_list: GetAllUsersResponseSchema, target_user: CreateUserResponseSchema):
    found_user = assert_single_match(user_list.users, "uuid", target_user.uuid, "User")

    assert_users_equal(found_user, target_user)


@allure.step("Check user not in list of users")
def assert_user_not_in_list(user_list: GetAllUsersResponseSchema, target_user: CreateUserResponseSchema):
    assert_zero_match(user_list.users, "uuid", target_user.uuid, "User")


@allure.step("Check user with uuid '{user_uuid}' not found error")
def assert_user_not_found_error(actual_error: ErrorSchema, user_uuid: str):
    expected_error = ErrorSchema(code=404, message=f'Could not find user with "uuid": {user_uuid}')
    assert_error_response(actual_error, expected_error)


@allure.step("Check user email '{email}' already taken error")
def assert_user_email_already_taken_error(actual_error: ErrorSchema, email: str):
    expected_error = ErrorSchema(code=409, message=f'User with the following "email" already exists: {email}')
    assert_error_response(actual_error, expected_error)
