from fastapi import FastAPI, Query, Depends
from typing import Optional
from datetime import date
from pydantic import BaseModel
from PETapp.bookings.router import router as router_bookings
from PETapp.users.router import router as router_users
from PETapp.hotels.router import router as router_hotels
from PETapp.hotels.rooms.router import router as router_rooms

app = FastAPI()

app.include_router(router_users)
app.include_router(router_bookings)
app.include_router(router_hotels)
app.include_router(router_rooms)

# class HotelsSearchArgs:
#     def __init__(
#             self,
#             location: str,
#             date_from: date,
#             date_to: date,
#             has_spa: Optional[bool] = None,
#             stars: Optional[int] = Query(None, ge=1, le=5),
#     ):
#         self.location = location
#         self.date_from = date_from
#         self.date_to = date_to
#         self.has_spa = has_spa
#         self.stars = stars


# @app.get("/hotels")
# def get_hotels(
#         search_args: HotelsSearchArgs = Depends()
# ):
#     return search_args

# class SBooking(BaseModel):
#     room_id: int
#     date_from: date
#     date_to: date
#
#
# @app.post("/bookings")
# def add_booking(booking: SBooking):
#     pass
