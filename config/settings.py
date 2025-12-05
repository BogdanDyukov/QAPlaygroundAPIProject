from pathlib import Path
from typing import Self
from pydantic import BaseModel, DirectoryPath, HttpUrl
from pydantic_settings import BaseSettings, SettingsConfigDict


class HTTPClientConfig(BaseModel):
    url: HttpUrl
    timeout: int

    @property
    def client_url(self) -> str:
        return str(self.url)


class Settings(BaseSettings):
    model_config = SettingsConfigDict(
        extra="allow",
        env_file=["./config/.env", "./config/.env.secret"],
        env_file_encoding="utf-8",
        env_nested_delimiter=".",
    )

    http_client: HTTPClientConfig
    bearer_token: str
    allure_results_dir: DirectoryPath

    @classmethod
    def initialize(cls) -> Self:
        allure_results_dir = Path("./allure-results")
        allure_results_dir.mkdir(exist_ok=True)

        return Settings(allure_results_dir=allure_results_dir)  # type: ignore


settings = Settings.initialize()
