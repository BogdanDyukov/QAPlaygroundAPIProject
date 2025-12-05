import allure
from requests import Response
from clients.common.api_client import APIClient
from clients.common.http_client_factory import get_http_client
from clients.users.routes import UsersRoutes
from clients.users.schema import CreateUserRequestSchema, GetAllUsersParamsSchema, UpdateUserRequestSchema


class UsersClient(APIClient):
    @allure.step("Create user")
    def create_user_api(self, user_payload: CreateUserRequestSchema) -> Response:
        return self.post(UsersRoutes.CREATE_USER, json=user_payload.model_dump())
    
    @allure.step("Get user by id")
    def get_user_by_id_api(self, user_uuid: str) -> Response:
        return self.get(UsersRoutes.GET_USER_BY_ID.format(user_uuid=user_uuid))
    
    @allure.step("Get all users")
    def get_all_users_api(self, params: GetAllUsersParamsSchema | None = None) -> Response:
        return self.get(UsersRoutes.GET_ALL_USERS, params=params.model_dump(exclude_none=True) if params else None)
    
    @allure.step("Update user")
    def update_user_api(self, user_uuid: str, update_data: UpdateUserRequestSchema) -> Response:
        return self.patch(
            UsersRoutes.UPDATE_USER.format(user_uuid=user_uuid), 
            json=update_data.model_dump(exclude_none=True)
        )

    @allure.step("Delete user")
    def delete_user_api(self, user_uuid: str) -> Response:
        return self.delete(UsersRoutes.DELETE_USER.format(user_uuid=user_uuid))


def get_users_client() -> UsersClient:
    return UsersClient(client=get_http_client())
