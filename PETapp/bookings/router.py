from datetime import date

from fastapi import APIRouter, Request, Depends
from sqlalchemy import Date

from PETapp.bookings.models import Bookings
from PETapp.bookings.service import BookingService
from PETapp.bookings.shemas import SBooking
from PETapp.exceptions import RoomCannotBeBooked
from PETapp.users.dependencies import get_current_user
from PETapp.users.models import Users

router = APIRouter(
    prefix="/bookings",
    tags=["Бронирования"]
)


@router.get("")
async def get_bookings(user: Users = Depends(get_current_user)):  # -> list[SBooking]:
    return await BookingService.find_all(user_id=user.id)


@router.post("")
async def add_booking(
        room_id: int,
        date_from: date,
        date_to: date,
        user: Users = Depends(get_current_user),
):
    booking = await BookingService.add(user.id, room_id, date_from, date_to)
    if not booking:
        raise RoomCannotBeBooked
