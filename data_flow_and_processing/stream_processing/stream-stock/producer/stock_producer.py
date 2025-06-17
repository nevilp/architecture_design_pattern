from kafka import KafkaProducer
import json, time, random

time.sleep(20)
producer = KafkaProducer(
    bootstrap_servers = 'kafka:9092',
    value_serializer = lambda v: json.dumps(v).encode('utf-8')
)

stocks = ["AAPL","NTFLX","TSLA","GOOG"]

while True:
    stock = random.choice(stocks)
    price = round(random.uniform(100,500),2)
    data = {"symbol":stock,"price":price,"timestamp":time.time()}
    producer.send("stock-prices",data)
    print(f'Produced: {data}')
    time.sleep(1)