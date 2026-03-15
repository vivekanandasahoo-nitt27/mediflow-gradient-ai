FROM python:3.10-slim

ENV PYTHONDONTWRITEBYTECODE=1
ENV PYTHONUNBUFFERED=1

# Install system dependencies
RUN apt-get update && apt-get install -y \
    ffmpeg \
    gcc \
    build-essential \
    libgl1 \
    libglib2.0-0 \
    git \
    && rm -rf /var/lib/apt/lists/*

WORKDIR /app

# Install Python dependencies
COPY requirements.txt .

RUN pip install --upgrade pip setuptools wheel
RUN pip install --default-timeout=1000 -r requirements.txt

# Copy project files
COPY . .

# Expose Gradio port
EXPOSE 7860

# Start application
CMD ["python", "app.py"]