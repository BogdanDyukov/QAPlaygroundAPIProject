import allure
from requests import Response
from clients.common.api_client import APIClient
from clients.common.http_client_factory import get_http_client
from clients.games.routes import GamesRoutes
from clients.games.schema import GetGamesByNameParamsSchema, GetAllGamesParamsSchema


class GamesClient(APIClient):
    @allure.step("Get all games")
    def get_all_games_api(self, params: GetAllGamesParamsSchema | None = None) -> Response:
        return self.get(GamesRoutes.GET_ALL_GAMES, params=params.model_dump(exclude_none=True) if params else None)

    @allure.step("Get games by name")
    def get_games_by_name_api(self, params: GetGamesByNameParamsSchema | None = None) -> Response:
        return self.get(GamesRoutes.GET_GAMES_BY_NAME, params=params.model_dump(exclude_none=True) if params else None)


def get_games_client() -> GamesClient:
    return GamesClient(client=get_http_client())
