# Image from dockerhub
FROM python:3.8-slim

ENV PYTHONUNBUFFERED 1

# Expose the port 8000 in which our application runs
EXPOSE 8000

# Make /code as a working directory in the container
WORKDIR /code

# Copy requirements from host, to docker container in /app
COPY ../requirements.txt /code/requirements.txt

# Install the dependencies
RUN pip install --no-cache-dir --upgrade -r requirements.txt

# Copy everything from ./src directory to /app in the container
COPY ../app /code/app




