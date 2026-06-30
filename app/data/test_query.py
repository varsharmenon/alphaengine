from app.database.database import SessionLocal
from app.database.models import Stock

session = SessionLocal()

stocks = session.query(Stock).all()

print(f"Number of stocks: {len(stocks)}")

print("First 5 stocks:")
for stock in stocks[:5]:
    print(stock.symbol, stock.company_name)

session.close()