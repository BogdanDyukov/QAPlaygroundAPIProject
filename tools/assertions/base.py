from typing import Any, Sized

import allure


@allure.step("Check that response status code equals to {expected}")
def assert_status_code(actual: int, expected: int):
    assert actual == expected, (
        f"Incorrect response status code. Expected status code: {expected}. Actual status code: {actual}"
    )


@allure.step("Check that {name} equals to {expected}")
def assert_equal(actual: Any, expected: Any, name: str):
    assert actual == expected, f'Incorrect value: "{name}". Expected value: {expected}. Actual value: {actual}'


@allure.step("Check that string contains {expected_substring}")
def assert_contains(actual_string: str, expected_substring: str):
    """
    Проверяет, что строка содержит подстроку.
    """
    assert expected_substring in actual_string, (
        f'String "{actual_string}" does not contain "{expected_substring}"'
    )


@allure.step("Check that list contains exactly one {name} with {attr} = {expected_value}")
def assert_single_match(items: list[Any], attr: str, expected_value: Any, name: str) -> Any:
    matched = [item for item in items if getattr(item, attr, None) == expected_value]

    assert matched, f"{name} with {attr}={expected_value} not found in list"
    assert len(matched) == 1, f"Expected exactly 1 {name} with {attr}={expected_value}, but found {len(matched)}"

    return matched[0]


@allure.step("Check that list doesn't contains {name} with {attr} = {expected_value}")
def assert_zero_match(items: list[Any], attr: str, expected_value: Any, name: str) -> Any:
    matched = [item for item in items if getattr(item, attr, None) == expected_value]

    assert not matched, f"{name} with {attr}={expected_value} found in list"
