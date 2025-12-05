from http import HTTPStatus

import allure
import pytest
from allure_commons.types import Severity

from clients.setup.setup_client import SetupClient
from clients.setup.schema import GetCurrentStatusResponseSchema
from tools.allure.epics import AllureEpic
from tools.allure.features import AllureFeature
from tools.allure.stories import AllureStory
from tools.assertions.base import assert_status_code


@pytest.mark.regression
@pytest.mark.setup
@allure.epic(AllureEpic.QA_PLAYGROUND)
@allure.feature(AllureFeature.SETUP)
class TestSetup:
    @allure.story(AllureStory.GET_ENTITY)
    @allure.title("Get current status")
    @allure.severity(Severity.NORMAL)
    def test_get_current_status(self, setup_client: SetupClient):
        get_current_status_response = setup_client.get_current_status_api()
        current_status = GetCurrentStatusResponseSchema.model_validate_json(get_current_status_response.text)

        assert_status_code(get_current_status_response.status_code, HTTPStatus.OK)
