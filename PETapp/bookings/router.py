from fastapi import APIRouter

from PETapp.bookings.service import BookingService
from PETapp.bookings.shemas import SBooking


router = APIRouter(
    prefix="/bookings",
    tags=["Бронирования"]
)


@router.get("")
async def get_bookings() -> list[SBooking]:
    return await BookingService.find_all()
