from sqlalchemy.ext.asyncio import create_async_engine
from sqlalchemy.ext.asyncio import AsyncSession
from sqlalchemy.ext.asyncio import async_sessionmaker
from sqlalchemy.ext.declarative import declarative_base

db_URL = "sqlite+aiosqlite:///./test.db"

engine = create_async_engine(db_URL,echo=True)

Session = async_sessionmaker(bind=engine,
                       class_=AsyncSession,
                        expire_on_commit=False)

Base = declarative_base()

async def init_db():
    async with engine.begin() as conn:
        await conn.run_sync(Base.metadata.create_all)

#get_db() type is generator
async def get_db():
    async with Session() as db:
        yield db
