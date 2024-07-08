from fastapi import APIRouter, Request, Depends

from PETapp.bookings.service import BookingService
from PETapp.bookings.shemas import SBooking
from PETapp.users.dependencies import get_current_user
from PETapp.users.models import Users

router = APIRouter(
    prefix="/bookings",
    tags=["Бронирования"]
)


@router.get("")
async def get_bookings(user: Users = Depends(get_current_user)): # -> list[SBooking]:
    return await BookingService.find_all(user_id=1)
    # return await BookingService.find_all()
