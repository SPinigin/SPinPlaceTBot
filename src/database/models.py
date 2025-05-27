from sqlalchemy import create_engine, Column, Integer, String, DateTime
from sqlalchemy.ext.declarative import declarative_base

Base = declarative_base()


class Booking(Base):
    __tablename__ = 'bookings'

    id = Column(Integer, primary_key=True)
    user_id = Column(Integer)
    check_in = Column(DateTime)
    check_out = Column(DateTime)
    guests = Column(Integer)
    contact_info = Column(String)
