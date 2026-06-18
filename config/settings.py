from pydantic import Field
from pydantic_settings import BaseSettings, SettingsConfigDict


class Settings(BaseSettings):
    """Centralized management of typed environment variables."""

    clickup_api_url: str = Field(
        default="https://api.clickup.com/api/v2",
        validation_alias="CLICKUP_API_URL",
    )

    clickup_api_token: str = Field(
        ...,
        validation_alias="CLICKUP_API_TOKEN",
    )

    env: str = Field(
        default="dev",
        validation_alias="ENV",
    )

    model_config = SettingsConfigDict(
        env_file=".env",
        env_file_encoding="utf-8",
        extra="ignore",
    )

app_settings = Settings()
