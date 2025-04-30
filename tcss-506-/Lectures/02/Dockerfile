# Use Python 3.11-slim as the base image
FROM python:3.11-slim

# Set the working directory inside the container
WORKDIR /app

# Copy the Flask application into the container
COPY app.py /app

# Install Flask and any required dependencies
RUN pip install --no-cache-dir flask

# Expose port 5000 for the Flask application
EXPOSE 5000

# Run the Flask application upon container startup
CMD ["python", "app.py"]