import json
import time
import csv
from kafka import KafkaProducer
from kafka.errors import NoBrokersAvailable

producer = None
for attempt in range(10):
    try:
        producer = KafkaProducer(
            bootstrap_servers='kafka1:9093,kafka2:9094',
            value_serializer=lambda v: json.dumps(v).encode('utf-8')
        )
        print("Kết nối Kafka thành công!")
        break
    except NoBrokersAvailable:
        print(f"Kafka broker chưa sẵn sàng, thử lại lần {attempt + 1} sau 5 giây...")
        time.sleep(5)

if not producer:
    raise Exception("Không kết nối được với Kafka broker sau nhiều lần thử!")

# Sau đó thực hiện gửi message
tweets_list = []
with open('/archive/1.csv', 'r', encoding='utf-8') as f:
    reader = csv.DictReader(f)
    for row in reader:
        tweets_list.append(row)

batch_size = 500
i = 0
while i < len(tweets_list):
    batch = tweets_list[i: i + batch_size]
    for tweet in batch:
        producer.send('tweets_stream', tweet)
        producer.send('tweets_batch', tweet)
    producer.flush()
    i += batch_size
    time.sleep(1)