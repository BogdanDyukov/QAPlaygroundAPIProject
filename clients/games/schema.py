from clients.common.schemas.base_schema import BaseSchema


class MetaSchema(BaseSchema):
    total: int


class GameSchema(BaseSchema):
    category_uuids: list[str]
    price: int
    title: str
    uuid: str


class GamesSchema(BaseSchema):
    games: list[GameSchema]
    meta: MetaSchema


class GetAllGamesResponseSchema(GamesSchema):
    pass


class GetAllGamesParamsSchema(BaseSchema):
    offset: int | None = None
    limit: int | None = None
    game_uuid_list: list[str] | None = None


class GetGamesByNameResponseSchema(GamesSchema):
    pass


class GetGamesByNameParamsSchema(BaseSchema):
    query: str | None = None
    offset: int | None = None
    limit: int | None = None
