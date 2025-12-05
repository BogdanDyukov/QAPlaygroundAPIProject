import allure
from requests import Response
from clients.common.api_client import APIClient
from clients.common.http_client_factory import get_http_client
from clients.wishlists.routes import WishlistsRoutes
from clients.wishlists.schema import AddItemToWishlistRequestSchema


class WishlistsClient(APIClient):
    @allure.step("Get user wishlist")
    def get_user_wishlist_api(self, user_uuid: str) -> Response:
        return self.get(WishlistsRoutes.GET_USER_WISHLIST.format(user_uuid=user_uuid))

    @allure.step("Add item to wishlist")
    def add_item_to_wishlist_api(self, user_uuid: str, game_uuid_payload: AddItemToWishlistRequestSchema) -> Response:
        return self.post(
            WishlistsRoutes.ADD_ITEM_TO_WISHLIST.format(user_uuid=user_uuid), json=game_uuid_payload.model_dump()
        )


def get_wishlists_client() -> WishlistsClient:
    return WishlistsClient(client=get_http_client())
