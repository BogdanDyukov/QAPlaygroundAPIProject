from pydantic import Field
from clients.common.schemas.base_schema import BaseSchema


class GetCurrentStatusResponseSchema(BaseSchema):
    task_id: str = Field(..., pattern=r"^api-([1-9]|[1-3][0-9]|40)$")  # api-1 до api-40 включительно
