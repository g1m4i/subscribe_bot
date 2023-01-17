import logging
from typing import Any

from sqlalchemy import URL
from sqlalchemy.ext.asyncio import AsyncSession, create_async_engine
from sqlalchemy.orm import sessionmaker

from src.config import DB

logger = logging.getLogger(__name__)


def make_connection_string(db: DB, async_fallback: bool = False) -> str:
    url = URL.create(
        drivername="postgresql+asyncpg",
        username=db.user,
        password=db.password,
        host=db.host,
        port=db.port,
        database=db.name,
    ).render_as_string(hide_password=False)

    if async_fallback:
        url += "?async_fallback=True"

    logger.debug(f"DB url {url}")
    return url


def sa_sessionmaker(connection_url: str, echo: bool = False) -> Any:
    engine = create_async_engine(connection_url, echo=echo)
    return sessionmaker(
        bind=engine,  # type: ignore
        expire_on_commit=False,
        class_=AsyncSession,
        future=True,
        autoflush=False,
    )
