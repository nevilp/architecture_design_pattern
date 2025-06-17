import asyncio
from fastapi import FastAPI ,WebSocket
from fastapi.middleware.cors import CORSMiddleware
import json
from kafka import KafkaConsumer
import time
import uvicorn

app = FastAPI()

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],  # or specific ["http://localhost:3000"]
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

topic="stock-prices"
print("starting consumer")
consumer = KafkaConsumer(topic,
                             bootstrap_servers='kafka:9092',
                              auto_offset_reset = 'earliest',
                               enable_auto_commit =True,
                                group_id ='commentry-group' )
print("consumer started")

@app.websocket("/ws/stockstream")
async def stock_streamer(websocket: WebSocket):
    print("websocket connection started")
    await websocket.accept()    
    try: 
        while True:
            msg_pack = consumer.poll(timeout_ms=1000)
            for tp, messages in msg_pack.items():
                for message in messages:
                    event = json.loads(message.value.decode('utf-8'))
                    print("Kafka message:", event)
                    await websocket.send_json(event)
            await asyncio.sleep(1)
    except Exception as e:
        print(f"Websocket connection closed {e}")
        await websocket.close()
    
if __name__ == '__main__':
   uvicorn.run(app,host='0.0.0.0',port=8000)