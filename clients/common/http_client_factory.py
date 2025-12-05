from clients.common.http_client import HTTPClient
from config.settings import settings


def get_http_client() -> HTTPClient:
    client = HTTPClient(base_url=settings.http_client.client_url, timeout=settings.http_client.timeout)

    client.headers.update(
        {
            "Authorization": f"Bearer {settings.bearer_token}",
            "X-Task-Id": "API-1",
        }
    )

    return client
