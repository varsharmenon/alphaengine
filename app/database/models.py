from sqlalchemy import Column, Integer, String
from .database import Base

class Stock(Base):
    __tablename__ = "stocks"

    id = Column(Integer, primary_key=True)

    symbol = Column(String, unique=True, index=True)

    company_name = Column(String)

    sector = Column(String)

    series = Column(String)

    isin_code = Column(String, unique=True)