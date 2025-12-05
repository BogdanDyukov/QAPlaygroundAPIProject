import allure
from clients.wishlists.schema import WishlistSchema
from tools.assertions.base import assert_single_match


@allure.step('Check that the user wishlist contains a game with a uuid: "{game_uuid}"')
def assert_user_wishlist_contains_game_uuid(game_uuid: str, user_wishlist: WishlistSchema):
    assert_single_match(user_wishlist.items, 'uuid', game_uuid, 'Game')
