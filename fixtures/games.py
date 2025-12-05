import pytest

from clients.games.games_client import GamesClient, get_games_client


@pytest.fixture
def games_client() -> GamesClient:
    return get_games_client()
