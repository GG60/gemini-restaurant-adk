# Use the official Python base image
FROM python:3.11-slim

# Set environment variables
ENV PYTHONUNBUFFERED True

# Install dependencies needed for ADK
# سنستخدم نسخة بسيطة من apt-get لتجنب تعقيدات apt-get install -y git
RUN apt-get update && apt-get install -y --no-install-recommends \
    build-essential \
    && rm -rf /var/lib/apt/lists/*

# Copy requirements.txt and install packages
COPY requirements.txt .

# ⚠️ التثبيت النظيف: نستخدم أمر pip واحد فقط لتثبيت كل شيء
RUN pip install --no-cache-dir -r requirements.txt 

# Copy the application code
COPY . /app
WORKDIR /app

# Expose port (ADK default port)
EXPOSE 8000
ENV PORT=8000
# Command to run the ADK Agent service (the standard ADK command)
# هذا الأمر يبدأ الخادم الصحيح ويفتح المنفذ 8000
CMD ["python", "-m", "adk", "run"]