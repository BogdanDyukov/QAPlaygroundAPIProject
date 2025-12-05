from http import HTTPStatus
import allure
import pytest
from allure_commons.types import Severity

from clients.games.games_client import GamesClient
from clients.games.schema import GetGamesByNameResponseSchema, GetGamesByNameParamsSchema
from tools.allure.epics import AllureEpic
from tools.allure.features import AllureFeature
from tools.allure.stories import AllureStory
from tools.assertions.base import assert_status_code
from tools.assertions.games import assert_search_results_are_relevant


@pytest.mark.regression
@pytest.mark.games
@allure.epic(AllureEpic.QA_PLAYGROUND)
@allure.feature(AllureFeature.GAMES)
class TestGames:
    @pytest.mark.parametrize('search_query', ['Atomic', ' ', 'fsagasgas'])
    @allure.story(AllureStory.GET_ENTITIES)
    @allure.title("Get games by name: '{search_query}'")
    @allure.severity(Severity.NORMAL)
    def test_get_games_by_name(self, search_query: str, games_client: GamesClient):

        get_games_by_name_params = GetGamesByNameParamsSchema(query=search_query)
        get_games_by_name_response = games_client.get_games_by_name_api(get_games_by_name_params)
        search_results = GetGamesByNameResponseSchema.model_validate_json(get_games_by_name_response.text)

        assert_status_code(get_games_by_name_response.status_code, HTTPStatus.OK)
        assert_search_results_are_relevant(search_results, search_query)
