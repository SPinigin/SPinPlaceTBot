from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from datetime import datetime
from .models import Base, Booking, User
from config.config import Config

engine = create_engine(Config.DATABASE_URL)
Session = sessionmaker(bind=engine)


class DatabaseManager:
    @staticmethod
    def init_db():
        Base.metadata.create_all(engine)

    @staticmethod
    def check_availability(check_in: datetime, check_out: datetime) -> bool:
        session = Session()
        existing_booking = session.query(Booking).filter(
            (Booking.check_in <= check_out) &
            (Booking.check_out >= check_in) &
            (Booking.status != 'cancelled')
        ).first()
        session.close()
        return existing_booking is None

    @staticmethod
    def create_booking(user_id: int, check_in: datetime, check_out: datetime,
                       guests: int, contact_info: str, total_price: float) -> Booking:
        session = Session()
        booking = Booking(
            user_id=user_id,
            check_in=check_in,
            check_out=check_out,
            guests=guests,
            contact_info=contact_info,
            total_price=total_price,
            status='pending'
        )
        session.add(booking)
        session.commit()
        session.close()
        return booking

    @staticmethod
    def get_user_bookings(user_id: int) -> list:
        session = Session()
        bookings = session.query(Booking).filter_by(user_id=user_id).all()
        session.close()
        return bookings
