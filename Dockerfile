# 1. Use a lightweight official Python image
FROM python:3.11-slim

# 2. Set the working directory inside the container
WORKDIR /app

# 3. Copy only the requirements first (caches dependencies)
COPY requirements.txt .

# 4. Install the Python dependencies
RUN pip install --no-cache-dir -r requirements.txt

# 5. Copy the rest of your application code
COPY app/ app/

# 6. Expose the port your Flask app runs on
EXPOSE 5000

# 7. Tell Docker how to run your application
CMD ["python", "app/app.py"]