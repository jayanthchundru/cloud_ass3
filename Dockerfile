FROM python:3.9-slim

# Set working directory
WORKDIR /home/data

# Copy only necessary files into the container
COPY script.py /home/data/
COPY IF-1.txt /home/data/
COPY AlwaysRememberUsThisWay-1.txt /home/data/

# Install only required dependencies
RUN pip install --no-cache-dir nltk

# Remove unnecessary package cache to reduce image size
RUN apt-get clean && rm -rf /var/lib/apt/lists/* /tmp/* /var/tmp/*

# Ensure output directory exists
RUN mkdir -p /home/data/output

# Use a more efficient CMD execution
CMD ["python3", "/home/data/script.py"]