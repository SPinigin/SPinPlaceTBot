from datetime import datetime
from sqlalchemy import create_engine, Column, Integer, String, DateTime, Boolean, Float
from sqlalchemy.ext.declarative import declarative_base

Base = declarative_base()


class Booking(Base):
    __tablename__ = 'bookings'

    id = Column(Integer, primary_key=True)
    user_id = Column(Integer)
    user_name = Column(String)
    check_in = Column(DateTime)
    check_out = Column(DateTime)
    guests = Column(Integer)
    contact_info = Column(String)
    total_price = Column(Float)
    deposit_paid = Column(Boolean, default=False)
    status = Column(String)  # 'pending', 'confirmed', 'cancelled'
    created_at = Column(DateTime, default=datetime.now)


class User(Base):
    __tablename__ = 'users'

    id = Column(Integer, primary_key=True)
    telegram_id = Column(Integer, unique=True)
    username = Column(String)
    full_name = Column(String)
    phone = Column(String)
    created_at = Column(DateTime, default=datetime.now)
