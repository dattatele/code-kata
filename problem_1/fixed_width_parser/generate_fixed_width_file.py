"""Generate a fixed width file based on the provided specification."""

import json
import os
import logging
from faker import Faker
from typing import List
from tqdm import tqdm

def main():
    # Ensure logs directory exists
    os.makedirs('logs', exist_ok=True)

    # Configure logging
    logging.basicConfig(
        filename='logs/generate_fixed_width.log',
        level=logging.INFO,
        format='%(asctime)s - %(levelname)s - %(message)s',
    )

    try:
        generate_fixed_width_file('spec.json', 'data/fixed_width_file.txt', num_records=1000)
    except Exception as e:
        logging.error(f"An error occurred: {e}")
        raise

def read_spec(spec_file: str) -> dict:
    """Read the specification from a JSON file.

    Args:
        spec_file (str): Path to the spec file.

    Returns:
        dict: Specification dictionary.
    """
    spec_file_path = os.path.join(os.path.dirname(__file__), '..', spec_file)
    try:
        with open(spec_file_path, 'r') as f:
            spec = json.load(f)
        logging.info(f"Specification file '{spec_file}' loaded successfully.")
        return spec
    except Exception as e:
        logging.error(f"Error reading specification file '{spec_file}': {e}")
        raise

def generate_field_data(fake: Faker, col_name: str) -> str:
    """Generate realistic data for a given column.

    Args:
        fake (Faker): Faker instance.
        col_name (str): Column name.

    Returns:
        str: Generated data.
    """
    field_generators = {
        'f1': fake.first_name,
        'f2': fake.last_name,
        'f3': fake.state_abbr,
        'f4': lambda: str(fake.random_digit_not_null()),
        'f5': fake.street_address,
        'f6': fake.city,
        'f7': fake.postcode,
        'f8': fake.country,
        'f9': fake.email,
        'f10': fake.phone_number,
    }
    generator = field_generators.get(col_name, fake.word)
    return generator()

def generate_fixed_width_file(spec_file: str, output_file: str, num_records: int = 1000) -> None:
    """Generate a fixed width file based on the specification.

    Args:
        spec_file (str): Path to the spec file.
        output_file (str): Path to the output fixed width file.
        num_records (int): Number of records to generate.
    """
    spec = read_spec(spec_file)
    encoding: str = spec['FixedWidthEncoding']
    include_header: bool = spec['IncludeHeader'].lower() == 'true'
    offsets: List[int] = [int(offset) for offset in spec['Offsets']]
    column_names: List[str] = spec['ColumnNames']

    fake = Faker()
    Faker.seed(0)

    # Ensure data directory exists
    os.makedirs(os.path.dirname(output_file), exist_ok=True)

    try:
        with open(output_file, 'w', encoding=encoding) as f:
            if include_header:
                header = ''.join(col_name.ljust(length) for col_name, length in zip(column_names, offsets))
                f.write(header + '\n')
            logging.info(f"Started generating fixed width file '{output_file}' with {num_records} records.")

            for _ in tqdm(range(num_records), desc="Generating fixed width records"):
                line = ''
                for col_name, length in zip(column_names, offsets):
                    data = generate_field_data(fake, col_name)
                    data = str(data)[:length].ljust(length)
                    line += data
                f.write(line + '\n')

            logging.info(f"Fixed width file '{output_file}' generated successfully.")
    except Exception as e:
        logging.error(f"Error generating fixed width file '{output_file}': {e}")
        raise

if __name__ == '__main__':
    main()
