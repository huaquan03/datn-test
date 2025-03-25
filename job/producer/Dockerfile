# Sử dụng image Python nhẹ
FROM python:3.11.4-slim


# Đặt thư mục làm việc
WORKDIR /app

# Copy file requirements (nếu có)
COPY requirements.txt .
# Ví dụ nội dung requirements.txt:
# kafka-python==2.0.2
RUN pip install --default-timeout=300 --no-cache-dir -r requirements.txt


# Copy file mã nguồn của producer
COPY producer.py .

# Command chạy producer
CMD ["python", "producer.py"]
