from datetime import datetime
import pytz

IST = pytz.timezone("Asia/Kolkata")

def convert_ist_to_timezone(dt_ist: datetime, tzname: str) -> datetime:
    """
    Converts a timezone-aware IST datetime to the requested timezone.
    """
    if dt_ist.tzinfo is None:
        dt_ist = IST.localize(dt_ist)
    target_tz = pytz.timezone(tzname)
    return dt_ist.astimezone(target_tz)
