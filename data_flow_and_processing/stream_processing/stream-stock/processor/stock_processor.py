import faust

from sqlalchemy import create_engine, Column, String, Float, Table, MetaData


class Stock(faust.Record):
    symbol:str
    price:float
    timestamp: float

app = faust.App('stock-processor',
                broker='kafka://localhost:9092',
                value_serializer='json') 

stock_topic = app.topic('stock-prices',value_type=Stock)
engine = create_engine("sqlite:///stocks.db")
metadata = MetaData()

stock_table = Table('stocks_symbol',metadata,Column('symbol',String),
                    Column('price',Float),
                    Column('timestamp',Float))
metadata.create_all(engine)
conn= engine.connect()

@app.agent(stock_topic)
async def process(stocks):
    async for stock in stocks:
        print( f"Processed: {stock.symbol} @ ₹{stock.price} at {stock.timestamp}")
        with engine.begin() as conn:  # Ensures commit
            conn.execute(stock_table.insert().values(
                symbol=stock.symbol,
                price=stock.price,
                timestamp=stock.timestamp
            ))
        

if __name__ == '__main__':
    app.main()        