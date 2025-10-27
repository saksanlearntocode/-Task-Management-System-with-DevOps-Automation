FROM python:3.9-slim

WORKDIR /app

COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

COPY . .

# Create data directory and set permissions
RUN mkdir -p /app/data && \
    chmod 777 /app/data

# Initialize the database
RUN python init_db.py

EXPOSE 5000

CMD ["python", "app.py"]
