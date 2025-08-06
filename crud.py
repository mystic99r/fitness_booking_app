from sqlalchemy.orm import Session
from models import FitnessClass, Booking
from datetime import datetime
import pytz

IST = pytz.timezone("Asia/Kolkata")

def get_classes(db: Session):
    """
    Fetches all upcoming fitness classes scheduled at or after current IST time.
    """
    now_ist = datetime.now(IST)
    return db.query(FitnessClass).filter(FitnessClass.datetime_ist >= now_ist).all()

def get_class(db: Session, class_id: int):
    """
    Retrieve a fitness class by its ID.
    """
    return db.query(FitnessClass).filter(FitnessClass.id == class_id).first()

def create_booking(db: Session, class_id: int, client_name: str, client_email: str):
    """
    Creates a booking for a given class if slots are available.
    Decrements available slots upon success.
    Raises ValueError if class not found or no slots available.
    """
    fitness_class = get_class(db, class_id)
    if not fitness_class:
        raise ValueError("Class not found")
    if fitness_class.available_slots <= 0:
        raise ValueError("No slots available for this class")

    fitness_class.available_slots -= 1

    booking = Booking(
        class_id=class_id,
        client_name=client_name,
        client_email=client_email,
    )
    db.add(booking)
    db.commit()
    db.refresh(booking)
    db.refresh(fitness_class)
    return booking

def get_bookings_by_email(db: Session, email: str):
    """
    Retrieves all bookings made by a specific client email.
    """
    return db.query(Booking).filter(Booking.client_email == email).all()
