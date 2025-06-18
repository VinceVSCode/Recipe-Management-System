# Dockerfile for a Python application
FROM python:3.11-slim

# Working directory
WORKDIR /app

# Copy requirements file
COPY . . 

# We install the requirements
RUN pip install --no-cache-dir -r requirements.txt || true

# Try runnning the main.py
CMD ["python", "main.py"]