from datetime import datetime, timedelta
from config.config import Config


def validate_dates(check_in: datetime, check_out: datetime) -> bool:
    now = datetime.now()
    stay_duration = (check_out - check_in).days

    return (
            check_in >= now and
            check_out > check_in and
            Config.MIN_BOOKING_DAYS <= stay_duration <= Config.MAX_BOOKING_DAYS
    )


def validate_guests(guests: int) -> bool:
    return 1 <= guests <= Config.MAX_GUESTS


def calculate_price(check_in: datetime, check_out: datetime, guests: int) -> float:
    base_price = 5000  # Базовая стоимость за сутки
    days = (check_out - check_in).days

    return base_price * days
