from pydantic_settings import BaseSettings, SettingsConfigDict
from pydantic import Field


class Settings(BaseSettings):
    """Centralized management of typed environment variables."""

    clickup_api_url: str = Field(
        default="https://api.clickup.com/api/v2",
        env="CLICKUP_API_URL",
    )

    clickup_api_token: str = Field(
        ...,
        env="CLICKUP_API_TOKEN",
    )

    env: str = Field(
        default="dev",
        env="ENV",
    )

    model_config = SettingsConfigDict(
        env_file=".env",
        env_file_encoding="utf-8",
        extra="ignore",
    )

app_settings = Settings()