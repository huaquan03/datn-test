from pyspark.sql import SparkSession 
from pyspark.sql import functions as F

# Khởi tạo SparkSession
spark = SparkSession.builder.appName("BatchProcessing").getOrCreate()
spark.conf.set("spark.sql.debug.maxToStringFields", 100)

# Đọc file Parquet với các tùy chọn giúp tránh lỗi header
df = spark.read.parquet("hdfs://namenode:9000/gmd.parquet")

# Hiển thị schema để kiểm tra
df.printSchema()
sum=0

total_volume_df = df.agg(F.sum("volume").alias("total_volume"))
total_volume_df.show()


print  ("Tổng số lượng cổ phiếu: ", sum)
# Loại bỏ dòng có text NULL


# Hiển thị kết quả

df.show(truncate=False)
# Chọn các cột cần thiết

# Đổi tên cột

# Nếu cần, lưu lại thành file Parquet để xử lý nhanh hơn lần sau
# processed_df.write.mode("overwrite").parquet("/data/processed_tweets/")

# Dừng Spark
spark.stop()
