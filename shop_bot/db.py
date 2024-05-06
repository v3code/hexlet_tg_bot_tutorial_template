from sqlalchemy.ext.asyncio import async_sessionmaker, create_async_engine

from shop_bot import config

engine = create_async_engine(config.DATABASE_URI, echo=config.IS_DEBUG)
async_session = async_sessionmaker(engine, expire_on_commit=False)
