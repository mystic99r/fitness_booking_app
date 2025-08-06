from fastapi import FastAPI, HTTPException, Depends, Query, Request
from fastapi.responses import JSONResponse
from sqlalchemy.orm import Session
from typing import List
import logging

import models, schemas, crud, seed, utils
from database import SessionLocal, engine
from pydantic import EmailStr

logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)

app = FastAPI(title="Fitness Studio Booking API")

models.Base.metadata.create_all(bind=engine)
seed.seed_data()

def get_db():
    """
    Dependency that yields a database session.
    """
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()

@app.exception_handler(ValueError)
async def value_error_exception_handler(request: Request, exc: ValueError):
    """
    Custom handler for ValueErrors to return 400 errors with detail.
    """
    logger.warning(f"ValueError: {exc}")
    return JSONResponse(status_code=400, content={"detail": str(exc)})

@app.get("/classes", response_model=List[schemas.FitnessClassOut])
def list_classes(
    tz: str = Query(default="Asia/Kolkata", description="Timezone name (e.g., UTC, America/New_York)"),
    db: Session = Depends(get_db),
):
    """
    Returns all upcoming fitness classes with times converted to given timezone.
    """
    classes = crud.get_classes(db)
    results = []
    for cls in classes:
        localized_datetime = utils.convert_ist_to_timezone(cls.datetime_ist, tz)
        results.append(schemas.FitnessClassOut(
            id=cls.id,
            name=cls.name,
            datetime=localized_datetime,
            instructor=cls.instructor,
            available_slots=cls.available_slots,
        ))
    logger.info(f"Returned {len(results)} classes in timezone {tz}")
    return results

@app.post("/book", response_model=schemas.BookingOut)
def book_spot(booking_req: schemas.BookingCreate, db: Session = Depends(get_db)):
    """
    Book a spot in a fitness class.
    Validates input and slot availability.
    """
    booking = crud.create_booking(db, booking_req.class_id, booking_req.client_name, booking_req.client_email)
    logger.info(f"Booking successful for class_id={booking_req.class_id}, client_email={booking_req.client_email}")
    return booking

@app.get("/bookings", response_model=List[schemas.BookingOut])
def get_bookings(
    client_email: EmailStr = Query(..., description="Client email to filter bookings"),
    db: Session = Depends(get_db),
):
    """
    Return all bookings made by the specified client email.
    """
    bookings = crud.get_bookings_by_email(db, client_email)
    logger.info(f"Returned {len(bookings)} bookings for {client_email}")
    return bookings
