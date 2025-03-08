# Use an official Python image
FROM python:3.9

# Set the working directory inside the container
WORKDIR /app

# Copy the requirements file and install dependencies
COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

# Copy the Python script into the container
COPY mlflow_lr.py .

# Run the script when the container starts
CMD ["python", "mlflow_lr.py"]
