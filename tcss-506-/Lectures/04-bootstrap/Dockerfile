# Use Python 3.11-slim as the base image
FROM python:3.11-slim

# Set the working directory inside the container
WORKDIR /app
RUN pip install --upgrade pip

# Copy the Flask application into the container
COPY app.py /app
COPY templates /app/templates

COPY requirements.txt /app/requirements.txt
RUN pip install -r requirements.txt

# Install Flask and any required dependencies
RUN pip install --no-cache-dir flask

# Expose port 5000 for the Flask application
EXPOSE 5000

# Run the Flask application upon container startup
CMD ["python", "app.py"]