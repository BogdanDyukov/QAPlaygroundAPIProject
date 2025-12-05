import allure
from clients.common.schemas.errors_schema import ErrorSchema
from tools.assertions.base import assert_equal


@allure.step("Check error response")
def assert_error_response(actual: ErrorSchema, expected: ErrorSchema):
    assert_equal(actual.code, expected.code, "Code")
    assert_equal(actual.message, expected.message, "Message")
    
