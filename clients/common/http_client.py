import allure
from requests import Response, Session
from tools.http.curl import make_curl_from_request

class HTTPClient(Session):
    """
    Низкоуровневый клиент (транспорт), который умеет говорить по протоколу HTTP.
    """
    def __init__(self, base_url, timeout=5):
        super().__init__()
        self.base_url = base_url
        self.timeout = timeout

    # Session.get() -> Session.request() -> Session.send()
    def request(self, method, url, **kwargs) -> Response:
        full_url = f"{self.base_url.rstrip('/')}/{url.lstrip('/')}"
        kwargs.setdefault("timeout", self.timeout)
        return super().request(method, full_url, **kwargs)

    def send(self, request, **kwargs):
        curl = make_curl_from_request(request)
        allure.attach(curl, "cURL", allure.attachment_type.TEXT)

        response = super().send(request, **kwargs)

        allure.attach(response.text, "Response", allure.attachment_type.TEXT)

        return response
