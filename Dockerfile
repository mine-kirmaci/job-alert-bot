# Python imajı
FROM python:3.11-slim

# Çalışma klasörü
WORKDIR /app

# Dosyaları kopyala
COPY . .

# Gerekli paketleri yükle
RUN pip install --no-cache-dir requests beautifulsoup4 python-dotenv

# Scripti çalıştır
CMD ["python", "job_alert.py"]