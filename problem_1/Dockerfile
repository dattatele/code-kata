# Use a base image with Python
FROM python:3.9-slim

# Set environment variables
ENV PYTHONDONTWRITEBYTECODE=1
ENV PYTHONUNBUFFERED=1

# Set the working directory
WORKDIR /app

# Install system dependencies
RUN apt-get update && \
    apt-get install -y --no-install-recommends \
        build-essential \
        libffi-dev \
        libssl-dev \
        gcc \
        make \
        && apt-get clean && rm -rf /var/lib/apt/lists/*

# Install Poetry
RUN pip install --no-cache-dir --upgrade pip setuptools wheel
RUN pip install --no-cache-dir poetry

# Copy only pyproject.toml and poetry.lock first to leverage Docker cache
COPY pyproject.toml poetry.lock ./

# Configure Poetry to not create virtual environments
RUN poetry config virtualenvs.create false

# Install dependencies, including dev dependencies
RUN poetry install --with dev

# Copy the rest of the application code
COPY . .

# Ensure logs directory exists
RUN mkdir -p logs

# Set the entry point
ENTRYPOINT ["bash", "-c"]

# Default command to run the scripts
CMD ["python fixed_width_parser/generate_fixed_width_file.py && python fixed_width_parser/parse_fixed_width_file.py"]
