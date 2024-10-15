# Fixed Width Parser

## Overview

This project generates a fixed width file based on a provided specification (`spec.json`) and parses it into a CSV file.

## Prerequisites

- **Docker** installed on your system.

## Running with Docker

### Build the Docker Image

```bash
docker build -t fixed-width-parser .
```
### Run the code

```bash
docker run --rm -v $(pwd)/data:/app/data fixed-width-parser

#with logs
docker run --rm -v $(pwd)/data:/app/data -v $(pwd)/logs:/app/logs fixed-width-parser

```
### Run the Tests
```bash
docker run --rm fixed-width-parser pytest --cov=fixed_width_parser tests/
```

##

### Project Structure

- fixed_width_parser/: Contains the main scripts.
- tests/: Contains the test scripts.
- data/: Directory for input and output files.
- spec.json: Specification file.
- Dockerfile: Docker image configuration.
- pyproject.toml & poetry.lock: Dependency management files.
- logs/: Directory for log files.
