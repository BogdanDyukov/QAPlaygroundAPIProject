from http import HTTPStatus
import allure
import pytest
from allure_commons.types import Severity

from clients.games.games_client import GamesClient
from clients.games.schema import GetAllGamesResponseSchema
from clients.wishlists.schema import AddItemToWishlistRequestSchema, GetUserWishlistResponseSchema
from clients.wishlists.wishlists_client import WishlistsClient
from fixtures.users import CreatedUserContext
from tools.allure.epics import AllureEpic
from tools.allure.features import AllureFeature
from tools.allure.stories import AllureStory
from tools.assertions.base import assert_status_code
from tools.assertions.wishlists import assert_user_wishlist_contains_game_uuid


@pytest.mark.regression
@pytest.mark.wishlists
@allure.epic(AllureEpic.QA_PLAYGROUND)
@allure.feature(AllureFeature.WISHLISTS)
class TestWishlists:
    @allure.story(AllureStory.CREATE_ENTITY)
    @allure.title("Add item to wishlist")
    @allure.severity(Severity.NORMAL)
    def test_add_item_to_wishlist(
        self, 
        wishlists_client: WishlistsClient, 
        games_client: GamesClient, 
        created_user_context: CreatedUserContext
    ):
        user_uuid = created_user_context.created_user.uuid

        get_all_games_response = games_client.get_all_games_api()
        games_list = GetAllGamesResponseSchema.model_validate_json(get_all_games_response.text)
        game_uuid = games_list.games[0].uuid

        game_uuid_payload = AddItemToWishlistRequestSchema(item_uuid=game_uuid)
        add_item_to_wishlist_response = wishlists_client.add_item_to_wishlist_api(user_uuid, game_uuid_payload)

        assert_status_code(add_item_to_wishlist_response.status_code, HTTPStatus.OK)

        get_user_wishlist_response = wishlists_client.get_user_wishlist_api(user_uuid)
        user_wishlist = GetUserWishlistResponseSchema.model_validate_json(get_user_wishlist_response.text)

        assert_status_code(get_user_wishlist_response.status_code, HTTPStatus.OK)
        assert_user_wishlist_contains_game_uuid(game_uuid, user_wishlist)
