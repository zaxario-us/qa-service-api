from pydantic_settings import BaseSettings, SettingsConfigDict


class DataBaseSettings(BaseSettings):
    model_config = SettingsConfigDict(
        env_prefix='db_'
    )

    user: str
    password: str
    database: str
    host: str
    port: int

    @property
    def connection_string(self) -> str:
        return f"postgresql+asyncpg://{self.user}:{self.password}@{self.host}:{self.port}/{self.database}"


class AppSettings(BaseSettings):
    model_config = SettingsConfigDict(
        env_prefix='app_'
    )

    host: str
    port: int
