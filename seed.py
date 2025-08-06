from database import SessionLocal, engine
import models
from datetime import datetime, timedelta
import pytz

IST = pytz.timezone("Asia/Kolkata")

def seed_data():
    models.Base.metadata.create_all(bind=engine)
    db = SessionLocal()

    # Check if already seeded
    count = db.query(models.FitnessClass).count()
    if count > 0:
        db.close()
        return

    # Use naive datetime and then localize it
    naive_now = datetime.now()  # naive datetime (no tzinfo)
    now_ist = IST.localize(naive_now)

    sample_classes = [
        models.FitnessClass(
            name="Yoga",
            datetime_ist=now_ist + timedelta(days=1, hours=6),
            instructor="Alice",
            total_slots=10,
            available_slots=10,
        ),
        models.FitnessClass(
            name="Zumba",
            datetime_ist=now_ist + timedelta(days=2, hours=12),
            instructor="Bob",
            total_slots=15,
            available_slots=15,
        ),
        models.FitnessClass(
            name="HIIT",
            datetime_ist=now_ist + timedelta(days=3, hours=18),
            instructor="Charlie",
            total_slots=20,
            available_slots=20,
        ),
    ]

    db.add_all(sample_classes)
    db.commit()
    db.close()
