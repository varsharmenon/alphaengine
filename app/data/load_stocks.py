import pandas as pd

from app.database.database import SessionLocal
from app.database.models import Stock


df = pd.read_csv("app/data/nifty500.csv")

session = SessionLocal()

try:
    for _, row in df.iterrows():
        symbol = row["Symbol"]

        stock = session.query(Stock).filter_by(symbol=symbol).first()
        if stock is None:
            stock = Stock(symbol=symbol)
            session.add(stock)

        stock.company_name = row["Company Name"]
        stock.sector = row["Industry"]
        stock.series = row["Series"]
        stock.isin_code = row["ISIN Code"]

    session.commit()
    print("Imported!")

finally:
    session.close()
