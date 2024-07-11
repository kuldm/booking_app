from sqlalchemy import select

from PETapp.database import async_session_maker
from PETapp.hotels.models import Hotels
from PETapp.services.base import BaseService


class HotelService(BaseService):
    model = Hotels

    # @classmethod
    # async def find_all(cls):
    #     async with async_session_maker() as session:
    #         get_all_hotels = select(Hotels)
    #         all_hotels = await session.execute(get_all_hotels)
    #         all_hotels = all_hotels.scalars().all()
    #         return all_hotels
