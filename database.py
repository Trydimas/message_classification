from sqlalchemy.ext.asyncio import async_sessionmaker, create_async_engine
from config import settings
from sqlalchemy.orm import DeclarativeBase, class_mapper

engine = create_async_engine(
    url=settings.DB_URL,
    pool_size=5,
    max_overflow=10
)

session_fa = async_sessionmaker(
    bind=engine,
    expire_on_commit=False
)


class Base(DeclarativeBase):

    def as_dict(self):
        columns = class_mapper(self.__class__).mapped_table.c
        return {col.name: getattr(self, col.name) for col in columns}


async def init_db():
    async with engine.begin() as conn:
        await conn.run_sync(Base.metadata.drop_all)
        await conn.run_sync(Base.metadata.create_all)


async def get_session():
    async with session_fa() as session:
        yield session
