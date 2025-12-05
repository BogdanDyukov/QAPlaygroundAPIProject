import allure
from clients.games.schema import GetGamesByNameResponseSchema
from tools.assertions.base import assert_contains


@allure.step('Check that all the games in the list contain a substring: "{search_query}"')
def assert_search_results_are_relevant(search_result: GetGamesByNameResponseSchema, search_query : str):
    for game in search_result.games:
        assert_contains(game.title, search_query)
