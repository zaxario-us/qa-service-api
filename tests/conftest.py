import pytest
import pytest_asyncio
from dotenv import load_dotenv

from src.database.db import settings
from src.database.models import Base

from sqlalchemy.ext.asyncio import create_async_engine, async_sessionmaker


def pytest_collection_modifyitems(config, items):
    load_dotenv()


@pytest_asyncio.fixture(scope="session")
async def async_engine():
    engine = create_async_engine(settings.get_connection_string(), echo=True)
    yield engine
    await engine.dispose()


@pytest_asyncio.fixture(scope="session")
async def async_session_maker(async_engine):
    async_session = async_sessionmaker(
        async_engine, expire_on_commit=False
    )
    yield async_session


@pytest_asyncio.fixture(scope="function")
async def db_session(async_engine, async_session_maker):
    async with async_engine.begin() as conn:
        await conn.run_sync(Base.metadata.drop_all)
        await conn.run_sync(Base.metadata.create_all)

    async with async_session_maker() as session:
        yield session

    async with async_engine.begin() as conn:
        await conn.run_sync(Base.metadata.drop_all)
        await conn.run_sync(Base.metadata.create_all)