from typing import Optional, List

from pydantic import BaseModel


class SRooms(BaseModel):
    id: int
    hotel_id: int
    name: str
    description: Optional[str]
    price: int
    quantity: int
    services: Optional[List[str]]
    image_id: Optional[int]

    class Config:
        from_attributes = True
