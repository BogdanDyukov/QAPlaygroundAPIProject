import requests
from shlex import quote


def make_curl_from_request(request: requests.PreparedRequest) -> str:
    from shlex import quote

    method = request.method
    url = request.url

    result = [f"curl -X {quote(method)} {quote(url)}"] # type: ignore

    # Заголовки
    for k, v in request.headers.items():
        result.append(f"-H {quote(f'{k}: {v}')}")

    # Тело
    if request.body:
        if isinstance(request.body, bytes):
            body = request.body.decode("utf-8", errors="replace")
        else:
            body = str(request.body)

        result.append(f"-d {quote(body)}")

    return " \\\n  ".join(result)
