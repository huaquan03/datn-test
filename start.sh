# Chạy Kafka stack
cd kafka && docker compose build --no-cache && docker compose up -d


# Chạy Spark cluster
cd ../spark && docker compose build --no-cache && docker compose up -d



# Chạy Jobs (Producer, Spark Streaming & Batch)
cd ../job && docker compose build --no-cache && docker compose up -d


# Chạy Serving layer
cd ../serving && docker compose build --no-cache && docker compose up -d

# Chạy hdfs
cd ../hdfs && docker compose build --no-cache && docker compose up -d