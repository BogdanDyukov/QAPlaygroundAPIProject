from pydantic import EmailStr, Field
from clients.common.schemas.base_schema import BaseSchema
from tools.fakers import fake


class UserSchema(BaseSchema):
    email: EmailStr
    name: str
    nickname: str
    avatar_url: str
    uuid: str


class MetaSchema(BaseSchema):
    total: int


class CreateUserRequestSchema(BaseSchema):
    email: EmailStr = Field(default_factory=fake.email)
    password: str = Field(default_factory=fake.password)
    name: str = Field(default_factory=fake.name)
    nickname: str = Field(default_factory=fake.nickname)


class CreateUserResponseSchema(UserSchema):
    pass


class UpdateUserRequestSchema(BaseSchema):
    email: EmailStr | None = Field(default_factory=fake.email)
    password: str | None = Field(default_factory=fake.password)
    name: str | None = Field(default_factory=fake.name)
    nickname: str | None = Field(default_factory=fake.nickname)


class GetUserByIdResponseSchema(UserSchema):
    pass


class GetAllUsersParamsSchema(BaseSchema):
    offset: int | None = None
    limit: int | None = None


class GetAllUsersResponseSchema(BaseSchema):
    meta: MetaSchema
    users: list[UserSchema]
