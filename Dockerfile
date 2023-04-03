# Set the base image
FROM python:3.10.6-slim-buster

# Install required system packages
RUN apt-get update && \
    apt-get install -y ffmpeg libsm6 libxext6
RUN apt-get install build-essential python3-dev -y
# Set the working directory
WORKDIR /app

# Copy the requirements file to the working directory
COPY . .

# Install the Python dependencies
RUN pip install --no-cache-dir -r requirements.txt

# Set the command to run the Python script
CMD [ "python", "main.py" ]