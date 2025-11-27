import asyncio

from database.db import engine
from database.models import Base


async def create_tables():
    async with engine.begin() as conn:
        while True:
            try:
                await conn.run_sync(Base.metadata.create_all)
                break
            except Exception as e:
                print(e)
                await asyncio.sleep(5)


async def drop_tables():
    async with engine.begin() as conn:
        await conn.run_sync(Base.metadata.drop_all)