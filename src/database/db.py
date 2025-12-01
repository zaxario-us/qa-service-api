from core.settings import DataBaseSettings
from sqlalchemy.ext.asyncio import create_async_engine, async_sessionmaker

database_settings = DataBaseSettings()
engine = create_async_engine(url=database_settings.connection_string)
new_session = async_sessionmaker(bind=engine, expire_on_commit=True)
