from typing import List

from fastapi import APIRouter
from starlette.responses import HTMLResponse

from PETapp.hotels.services import HotelService
from PETapp.hotels.shemas import SHotel

router = APIRouter(
    prefix="/hotels",
    tags=["Отели"],
)


@router.get("",
            response_model=List[SHotel],
            description="This method returns a list of all hotels",
            )
async def get_all_hotels():
    return await HotelService.find_all()
