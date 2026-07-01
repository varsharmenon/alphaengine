from sqlalchemy import Column, Date, Float, ForeignKey, Integer, String
from sqlalchemy.orm import relationship

from .database import Base

class Stock(Base):
    __tablename__ = "stocks"

    id = Column(Integer, primary_key=True)

    symbol = Column(String, unique=True, index=True)

    company_name = Column(String)

    sector = Column(String)

    series = Column(String)

    isin_code = Column(String, unique=True)

    prices = relationship("Price", back_populates="stock")


class Price(Base):
    __tablename__ = "prices"

    id = Column(Integer, primary_key=True)

    stock_id = Column(Integer, ForeignKey("stocks.id"), nullable=False, index=True)

    date = Column(Date)

    open = Column(Float)
    high = Column(Float)
    low = Column(Float)
    close = Column(Float)

    volume = Column(Integer)

    stock = relationship("Stock", back_populates="prices")