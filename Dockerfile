# Use the official Python 3.10 base image
FROM python:3.10

# Set the working directory inside the container
WORKDIR /app

# Install required packages
RUN pip install flask pymongo pytest

# Copy your Python script and other necessary files into the container
COPY . /app

# Expose port 5000
EXPOSE 5000

# Set the default command to execute
CMD ["main.py"]

# Set the entrypoint as Python
ENTRYPOINT ["python"]
