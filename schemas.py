from pydantic import BaseModel, EmailStr, Field
from datetime import datetime

class FitnessClassBase(BaseModel):
    name: str
    datetime: datetime
    instructor: str
    available_slots: int

    class Config:
        orm_mode = True

class FitnessClassOut(FitnessClassBase):
    id: int

class BookingCreate(BaseModel):
    class_id: int = Field(..., gt=0)
    client_name: str = Field(..., min_length=1)
    client_email: EmailStr

class BookingOut(BaseModel):
    id: int
    class_id: int
    client_name: str
    client_email: EmailStr

    class Config:
        orm_mode = True
