# Use an official Python runtime as a base image
FROM python:3.9-slim

# Set the working directory
WORKDIR /app

# Copy the current directory contents into the container at /app
COPY . /app

# Install Flask
RUN pip install --no-cache-dir flask

# Make port 8080 available to the world outside this container
EXPOSE 8081

# Run app.py when the container launches
CMD ["python", "app.py"]
