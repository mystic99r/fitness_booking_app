from sqlalchemy import Column, Integer, String, DateTime, ForeignKey
from sqlalchemy.orm import relationship
from database import Base

class FitnessClass(Base):
    __tablename__ = "fitness_classes"

    id = Column(Integer, primary_key=True, index=True)
    name = Column(String, index=True)
    datetime_ist = Column(DateTime)  # Stored in IST timezone
    instructor = Column(String)
    total_slots = Column(Integer)
    available_slots = Column(Integer)

    bookings = relationship("Booking", back_populates="fitness_class")


class Booking(Base):
    __tablename__ = "bookings"

    id = Column(Integer, primary_key=True, index=True)
    class_id = Column(Integer, ForeignKey("fitness_classes.id"))
    client_name = Column(String)
    client_email = Column(String, index=True)

    fitness_class = relationship("FitnessClass", back_populates="bookings")
