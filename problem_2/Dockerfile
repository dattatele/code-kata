# Use a base image with both Java and Python
FROM openjdk:17-slim

# Install Python and necessary packages
RUN apt-get update && \
    apt-get install -y --no-install-recommends \
        python3 \
        python3-pip \
        procps \
    && apt-get clean && rm -rf /var/lib/apt/lists/*

# Set the working directory
WORKDIR /app

# Copy requirements.txt
COPY requirements.txt ./

# Upgrade pip, setuptools, and wheel
RUN pip3 install --no-cache-dir --upgrade pip setuptools wheel

# Install dependencies
RUN pip3 install --no-cache-dir -r requirements.txt

# Copy application code
COPY data_processing/ data_processing/
COPY tests/ tests/

# Set environment variables for PySpark
ENV PYSPARK_PYTHON=python3
ENV PYSPARK_DRIVER_PYTHON=python3

# Set the entry point to bash
ENTRYPOINT ["bash", "-c"]

# Default command
CMD ["python3 data_processing/generate_large_csv.py && python3 data_processing/anonymize_data.py"]
