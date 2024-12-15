# Dockerfile
FROM python:3.9-slim

# Install dependencies
RUN apt-get update && apt-get install -y \
    build-essential \
    && rm -rf /var/lib/apt/lists/*

# Install Python packages
COPY requirements.txt requirements.txt
RUN pip install --no-cache-dir -r requirements.txt

# Expose ports for MLFlow and Streamlit
EXPOSE 5000 8501

# Set the working directory
WORKDIR /app
COPY . /app

# Default command
CMD ["streamlit", "run", "app.py"]