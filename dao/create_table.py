from core import Settings
from database import engine


async def create_tables() -> None:
    from models import CourseModel
    print(f"[+] Creating tables in database {CourseModel.__tablename__}")

    async with engine.begin() as conn:
        await conn.run_sync(Settings.DB_BASE_MODEL.metadata.drop_all)
        await conn.run_sync(Settings.DB_BASE_MODEL.metadata.create_all)
    print("[+] Success")


if __name__ == '__main__':
    import asyncio

    asyncio.run(create_tables())
