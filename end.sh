# Chạy Kafka stack
cd kafka && docker compose down

# Chạy Spark cluster
cd ../spark && docker compose down

# Chạy Jobs (Producer, Spark Streaming & Batch)
cd ../job && docker compose down

# Chạy Serving layer
cd ../serving && docker compose down

# Chạy hdfs
cd ../hdfs && docker compose down
