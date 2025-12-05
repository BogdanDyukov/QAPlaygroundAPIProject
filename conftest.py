import pytest

from clients.setup.setup_client import get_setup_client


pytest_plugins = (
    "fixtures.setup",
    "fixtures.users",
    "fixtures.games",
    "fixtures.wishlists",
    "fixtures.allure"
)


@pytest.fixture(scope="session", autouse=True)
def initialize_api():
    get_setup_client().setup_api()
    print("Тестовая среда инициализирована")
