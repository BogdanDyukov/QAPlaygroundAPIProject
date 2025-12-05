from pydantic import BaseModel


class BaseSchema(BaseModel):
    model_config = {"strict": True}
