
cd stream_processing/stream-stock 

python3 producer/stock_producer.py

faust -A processor.stock_processor worker -l info