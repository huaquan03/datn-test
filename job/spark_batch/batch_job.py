from pyspark.sql import SparkSession

# Khởi tạo SparkSession
spark = SparkSession.builder.appName("TweetBatchProcessing").getOrCreate()
spark.conf.set("spark.sql.debug.maxToStringFields", 100)

# Đọc file CSV với các tùy chọn giúp tránh lỗi header
df = spark.read.option("header", "true") \
               .option("inferSchema", "true") \
               .option("multiLine", "true") \
               .option("escape", "\"") \
               .option("mode", "DROPMALFORMED") \
               .option("ignoreLeadingWhiteSpace", "true") \
               .option("ignoreTrailingWhiteSpace", "true") \
               .csv("/archive/1.csv")

# Hiển thị schema để kiểm tra
df.printSchema()

# Loại bỏ dòng có text NULL
processed_df = df.filter(df.text.isNotNull())

# Hiển thị kết quả
processed_df.show(truncate=False)

# Nếu cần, lưu lại thành file Parquet để xử lý nhanh hơn lần sau
# processed_df.write.mode("overwrite").parquet("/data/processed_tweets/")

# Dừng Spark
spark.stop()
