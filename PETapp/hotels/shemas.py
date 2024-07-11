from typing import Optional, Dict, Any, List

from pydantic import BaseModel, Json


class SHotel(BaseModel):
    id: int
    name: str
    location: str
    services: Optional[List[str]]
    rooms_quantity: int
    image_id: Optional[int]

    class Config:
        from_attributes = True
