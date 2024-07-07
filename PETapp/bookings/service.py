from PETapp.database import async_session_maker
from sqlalchemy import select
from PETapp.bookings.models import Bookings
from PETapp.services.base import BaseService


class BookingService(BaseService):
    model = Bookings