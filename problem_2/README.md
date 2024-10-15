# Data Processing

## Overview

This project generates a large CSV file containing personal information and anonymizes specified columns using PySpark.

## Prerequisites

- **Docker** installed on your system.

## Running with Docker

### Build the Docker Image

```bash
docker build -t data-processing .
```
### Run the code

```bash
docker run --rm -v $(pwd)/data:/app/data data-processing
```
### Run the Tests
```bash
docker run --rm data-processing pytest --cov=data_processing tests/
```
##

### Project Structure

- data_processing/: Contains the main scripts.
- tests/: Contains the test scripts.
- data/: Directory for input and output files.
- Dockerfile: Docker image configuration.

