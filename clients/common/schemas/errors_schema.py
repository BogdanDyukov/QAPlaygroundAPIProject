from clients.common.schemas.base_schema import BaseSchema


class ErrorSchema(BaseSchema):
    code: int
    message: str
