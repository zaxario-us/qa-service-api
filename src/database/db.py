from os import environ

from sqlalchemy.ext.asyncio import create_async_engine, async_sessionmaker


class Settings:
    def __init__(self) -> None:
        self.user = environ.get("DB_USER")
        self.password = environ.get("DB_PASSWORD")
        self.database = environ.get("DB_DATABASE")
        self.host = environ.get("DB_HOST")
        self.port = environ.get("DB_PORT")

    @property
    def connection_string(self) -> str:
        return f"postgresql+asyncpg://{self.user}:{self.password}@{self.host}:{self.port}/{self.database}"


settings = Settings()

engine = create_async_engine(url=settings.connection_string)
new_session = async_sessionmaker(bind=engine, expire_on_commit=True)
