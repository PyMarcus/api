from typing import Generator
from sqlalchemy.ext.asyncio import AsyncSession
from dao import Session
from log import RotatingLog
from core import Settings


async def get_session() -> Generator:
    session: AsyncSession = Session()
    try:
        yield session
    except Exception as e:
        rl = RotatingLog(Settings.LOG_FILE, Settings.LOG_FILE, "error")
        rl.logger.error(e)
    finally:
        await session.close()
