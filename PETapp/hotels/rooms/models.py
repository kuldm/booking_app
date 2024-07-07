from sqlalchemy import Column, Integer, String, JSON, ForeignKey

from PETapp.database import Base


class Rooms(Base):
    __tablename__ = "rooms"

    id = Column(Integer, primary_key=True, nullable=False)
    hotel_id = Column(ForeignKey("hotels.id"), nullable=False)
    name = Column(String, nullable=False)
    description = Column(String, nullable=True)
    price = Column(Integer, nullable=False)
    quantity = Column(Integer, nullable=False)
    services = Column(JSON, nullable=True)
    image_id = Column(Integer)
