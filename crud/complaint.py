from sqlalchemy.ext.asyncio import AsyncSession

from models.complaints import ComplaintDB
from sqlalchemy import select

async def create_complaint(session: AsyncSession, body: ComplaintDB):
    session.add(body)
    await session.commit()
    await session.refresh(body)
    return body


async def get_all_complaint(session: AsyncSession):
    stmt = select(ComplaintDB)
    query = await session.execute(stmt)
    return query.scalars().all()
