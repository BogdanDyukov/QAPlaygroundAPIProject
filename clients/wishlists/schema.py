from clients.common.schemas.base_schema import BaseSchema
from clients.games.schema import GameSchema


class WishlistSchema(BaseSchema):
    items: list[GameSchema]
    user_uuid: str

class GetUserWishlistResponseSchema(WishlistSchema):
    pass


class AddItemToWishlistRequestSchema(BaseSchema):
    item_uuid: str


class AddItemToWishlistResponseSchema(WishlistSchema):
    pass
