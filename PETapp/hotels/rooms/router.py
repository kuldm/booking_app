from typing import List

from fastapi import APIRouter

from PETapp.hotels.rooms.services import RoomsService
from PETapp.hotels.rooms.shemas import SRooms

router = APIRouter(
    prefix="/hotels",
    tags=["Номера отелей"],
)


@router.get("/rooms",
            response_model=List[SRooms],
            description="This method returns all roms in all hotels",
            )
async def get_all_rooms():
    return await RoomsService.find_all()


@router.get("/{hotel_id}/rooms",
            response_model=List[SRooms],
            description="This method returns all roms in one hotel",
            )
async def get_rooms(hotel_id: int):
    return await RoomsService.find_all_rooms_by_hotel_id(hotel_id)
