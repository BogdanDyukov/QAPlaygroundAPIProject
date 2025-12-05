import pytest

from clients.wishlists.wishlists_client import WishlistsClient, get_wishlists_client


@pytest.fixture
def wishlists_client() -> WishlistsClient:
    return get_wishlists_client()
