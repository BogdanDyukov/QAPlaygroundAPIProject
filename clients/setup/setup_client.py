import allure
from requests import Response
from clients.common.api_client import APIClient
from clients.common.http_client_factory import get_http_client
from clients.setup.routes import SetupRoutes


class SetupClient(APIClient):
    """
    Клиент предметной области (доменный слой) - знает конкретные маршруты (/users/me) и схемы
    Инициирует запросы на уровне бизнес‑логики
    """
    @allure.step("API Setup")
    def setup_api(self) -> Response:
        return self.post(SetupRoutes.SETUP)

    @allure.step("Get current status")
    def get_current_status_api(self) -> Response:
        return self.get(SetupRoutes.STATUS)


def get_setup_client() -> SetupClient:
    return SetupClient(client=get_http_client())
