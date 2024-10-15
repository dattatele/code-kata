# Data Engineering Coding Challenges


## Overview

This repository contains solutions to two related problems:

1. **Problem 1:** Generate a fixed-width file based on a provided specification and parse it into a CSV file.
2. **Problem 2:** Generate a Large CSV file around 2 GB in size and then anonymize data points.

Both problems are implemented in Python, leveraging tools like Poetry for dependency management and Docker for containerization. Comprehensive testing ensures code reliability and coverage.

---

## Table of Contents

- [Prerequisites](#prerequisites)
- [Project Structure](#project-structure)
- [Problem 1: Fixed Width Parser](#problem-1-fixed-width-parser)
  - [Running Locally with Poetry](#running-locally-with-poetry)
  - [Running with Docker](#running-with-docker)
  - [Running Tests](#running-tests)
- [Problem 2: data processing](#problem-2-add-description)
  - [Running Locally with Poetry](#running-locally-with-poetry)
  - [Running with Docker](#running-with-docker)
  - [Running Tests](#running-tests)


---
# Problem 1: Fixed Width Parser and Analyzer



## Prerequisites

Ensure you have the following installed on your system:

- **Docker:** [Install Docker](https://docs.docker.com/get-docker/)
- **Poetry:** [Install Poetry](https://python-poetry.org/docs/#installation) (optional, for local development)

---

## Project Structure

problem_1/   
├── fixed_width_parser/       
│ ├── init.py     
│ ├── generate_fixed_width_file.py     
│ ├── parse_fixed_width_file.py     
│ └── ...    
├── tests/    
│ ├── test_generate_field_data.py     
│ ├── test_generate_fixed_width_file.py    
│ ├── test_parse_fixed_width_file.py    
│ └── ...    
├── data/    
│ └── (Generated data files)    
├── logs/    
│ └── (Log files)    
├── .gitignore    
├── pyproject.toml   
├── poetry.lock    
├── Dockerfile    
└── README.md   


- **`fixed_width_parser/`**: Contains the main Python scripts for generating and parsing fixed-width files.
- **`tests/`**: Contains test scripts to ensure the functionality and coverage of the code.
- **`data/`**: Stores input and output data files. This directory is ignored by Git to prevent accidental commits.
- **`logs/`**: Stores log files generated by the scripts. This directory is also ignored by Git.
- **`.gitignore`**: Specifies intentionally untracked files to ignore.
- **`pyproject.toml` & `poetry.lock`**: Manage project dependencies and configurations using Poetry.
- **`Dockerfile`**: Defines the Docker image configuration for containerizing the application.
- **`README.md`**: Provides an overview and instructions for the project.

---

## Problem 1: Fixed Width Parser

- Generate a fixed width file using the provided spec (offset provided in the spec file represent the length of each field).
- Implement a parser that can parse the fixed width file and generate a delimited file, like CSV for example.
- DO NOT use python libraries like pandas for parsing. You can use the standard library to write out a csv file (If you feel like)
- Language choices (Python or Scala)
- Deliver source via github or bitbucket
- Bonus points if you deliver a docker container (Dockerfile) that can be used to run the code (too lazy to install stuff that you might use)
- Pay attention to encoding


### **Overview**

Problem 1 involves generating a fixed-width file based on a JSON specification and then parsing that file into a CSV format. The process includes:

1. **Generating the Fixed Width File:**
   - Reads specifications from `spec.json`.
   - Uses the Faker library to generate realistic data.
   - Creates a fixed-width formatted file with or without headers.

2. **Parsing the Fixed Width File:**
   - Reads the fixed-width file based on `spec.json`.
   - Converts the data into a CSV file with appropriate headers.

### **Running Locally with Poetry**

If you prefer to run the scripts on your local machine without Docker, follow these steps:

1. **Clone the Repository:**

   ```bash
   cd problem_1
   ```

2. **Prerequisite:

Ensure Poetry is installed. If not, install it from Poetry Installation Guide. https://python-poetry.org/docs/

```bash
pip3 install poetry
```

### Running locally

3. Install Dependencies with Poetry

```bash
poetry install --with dev
```
##

- Generate Fixed Width File:

```bash
poetry run python fixed_width_parser/generate_fixed_width_file.py
```

- Parse Fixed Width File to CSV:

```bash
poetry run python fixed_width_parser/parse_fixed_width_file.py
```
- Check Outputs:

   -- Data Files: Generated fixed-width and CSV files will be in the data/ directory.
 
   -- Logs: Logs will be in the logs/ directory.

- Run test locally

```bash
poetry run pytest --cov=fixed_width_parser tests/
```

##

### Running with Docker

1. Build the Docker Image:

Ensure you're in the root directory of the project (problem_1/).

```bash
docker build -t fixed-width-parser .
```

2. Run the Scripts Inside Docker:
This command mounts the data/ and logs/ directories to your host machine, ensuring generated files and logs are accessible.
```bash
docker run --rm \
    -v $(pwd)/data:/app/data \
    -v $(pwd)/logs:/app/logs \
    fixed-width-parser
```
3. Run Tests with Coverage Inside Docker:

```bash
docker run --rm fixed-width-parser pytest --cov=fixed_width_parser tests/

```
##

# Problem 2: Data processing

- Generate a csv file containing first_name, last_name, address, date_of_birth
- Process the csv file to anonymise the data
- Columns to anonymise are first_name, last_name and address
- You might be thinking  that is silly
- Now make this work on 2GB csv file (should be doable on a laptop)
- Demonstrate that the same can work on bigger dataset
- Hint - You would need some distributed computing platform

##

- **`data_processing/`**: Contains the main Python scripts for generating large csv file and anonymizing data.
- **`tests/`**: Contains test scripts to ensure the functionality and coverage of the code.
- **`data/`**: Stores input and output data files. This directory is ignored by Git to prevent accidental commits.
- **`logs/`**: Stores log files generated by the scripts. This directory is also ignored by Git.
- **`.gitignore`**: Specifies intentionally untracked files to ignore.
- **`pyproject.toml` & `poetry.lock`**: Manage project dependencies and configurations using Poetry.
- **`Dockerfile`**: Defines the Docker image configuration for containerizing the application.
- **`README.md`**: Provides an overview and instructions for the project.


## Prerequisites

- **Docker** installed on your system.

## Running locally

### Running locally

1. Install Dependencies with Poetry
Ensure you're in the root directory of the project (problem_2/)

```bash
poetry install --with dev
```
##

- Generate Large 2 GB CSV file:

```bash
poetry run python data_processing/generate_large_csv.py
```

- Anonymize data:

```bash
poetry run python data_processing/anonymize_data.py
```
- Check Outputs:

   -- Data Files: Generated large CSV files will be in the data/ directory.
   -- anonymize data would be inside problem_2/data/anonymized_output/
 
   -- Logs: Logs will be in the logs/ directory.

- Running test locally

```bash
poetry run pytest --cov=data_processing tests/
```

##

### Running with Docker

1. Build the Docker Image

```bash
docker build -t data-processing .
```
2. Run the code

```bash
docker run --rm -v $(pwd)/data:/app/data data-processing
```
3.  Run the Tests
```bash
docker run --rm data-processing pytest --cov=data_processing tests/
```


##

# Data Engineering Coding Challenges

## Judgment Criteria

- Beauty of the code (beauty lies in the eyes of the beholder)
- Testing strategies
- Basic Engineering principles

## Choices

- Any language, any platform
- One of the above problems or both, if you feel like it.

