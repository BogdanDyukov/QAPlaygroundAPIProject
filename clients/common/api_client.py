from typing import Any

import allure
from requests import Response
from clients.common.http_client_factory import HTTPClient


class APIClient:
    """
    Клиент (базовый слой) - универсальная обёртка над транспортом
    Инициирует запросы  на уровне «API‑методов», а не чистого HTTP
    """
    def __init__(self, client: HTTPClient) -> None:
        self.client = client
    
    @allure.step("Make GET request to {url}")
    def get(self, url: str | bytes, params: dict[str, Any] | None = None) -> Response:
        return self.client.get(url, params=params)
    
    @allure.step("Make POST request to {url}")
    def post(self, url: str | bytes, json: Any | None = None) -> Response:
        return self.client.post(url, json=json)

    @allure.step("Make PATCH request to {url}")
    def patch(self, url: str | bytes, json: Any | None = None) -> Response:
        return self.client.patch(url, json=json)
    
    @allure.step("Make DELETE request to {url}")
    def delete(self, url: str | bytes) -> Response:
        return self.client.delete(url)
