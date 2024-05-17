
# syntax=docker/dockerfile:1
FROM ubuntu:20.04

# Install app dependencies
# Install libraries
RUN apt-get update && apt-get install -y python3-pip
RUN pip install python-dotenv
RUN pip install requests
RUN apt-get install python3-mysql.connector -y

# Install app
WORKDIR /app
COPY app.py .


