import pytest

from clients.setup.setup_client import SetupClient, get_setup_client


@pytest.fixture
def setup_client() -> SetupClient:
    return get_setup_client()
