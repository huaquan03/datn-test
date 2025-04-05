from pyspark.sql import SparkSession
from vnstock import Vnstock

# 1. Khởi tạo SparkSession
spark = SparkSession.builder \
    .appName("WriteParquetToHDFS") \
    .getOrCreate()

# 2. Lấy dữ liệu qua vnstock
stock = Vnstock().stock(symbol='GMD', source='VCI')
df_pandas = stock.quote.history(start='2000-03-29', end='2025-04-02', interval='1M')

# 3. Chuyển từ pandas DataFrame sang Spark DataFradf_spark = spark.createDataFrame(df_pandas)

# 4. Ghi DataFrame Spark lên HDFS dưới dạng Parquet
df_spark = spark.createDataFrame(df_pandas)

df_spark.write.mode("overwrite").parquet("hdfs://namenode:9000/gmd.parquet")

#    Nếu bạn muốn ghi dưới dạng CSV, có thể sử dụng đoạn mã sau:

# 5. Dừng SparkSession
spark.stop()
