from pydantic_settings import BaseSettings, SettingsConfigDict


class Settings(BaseSettings):
    debug: bool = False
    db_connection: str
    model_config = SettingsConfigDict(env_file=".env")


settings = Settings()
