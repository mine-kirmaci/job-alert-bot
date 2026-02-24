# Base image
FROM python:3.11-slim

# Güvenlik için non-root user
RUN useradd -m appuser

WORKDIR /app

# Önce sadece requirements kopyala (cache için)
COPY requirements.txt .

# Paketleri yükle
RUN pip install --no-cache-dir -r requirements.txt

# Sonra kodu kopyala
COPY . .

# Yetkiyi değiştir
RUN chown -R appuser:appuser /app
USER appuser

ENV PYTHONUNBUFFERED=1

CMD ["python", "job_alert.py"]