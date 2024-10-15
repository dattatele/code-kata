"""Parse a fixed width file and output a CSV file."""

import json
import csv
import os
import logging
from typing import List, Tuple
from tqdm import tqdm

def main():
    # Ensure logs directory exists
    os.makedirs('logs', exist_ok=True)

    # Configure logging
    logging.basicConfig(
        filename='logs/parse_fixed_width.log',
        level=logging.INFO,
        format='%(asctime)s - %(levelname)s - %(message)s',
    )

    try:
        parse_fixed_width_file('spec.json', 'data/fixed_width_file.txt', 'data/output.csv')
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
    try:
        with open(spec_file, 'r') as f:
            spec = json.load(f)
        logging.info(f"Specification file '{spec_file}' loaded successfully.")
        return spec
    except Exception as e:
        logging.error(f"Error reading specification file '{spec_file}': {e}")
        raise

def parse_fixed_width_file(spec_file: str, input_file: str, output_file: str) -> None:
    """Parse the fixed width file and output a CSV file.

    Args:
        spec_file (str): Path to the spec file.
        input_file (str): Path to the input fixed width file.
        output_file (str): Path to the output CSV file.
    """
    spec = read_spec(spec_file)
    encoding: str = spec['FixedWidthEncoding']
    delimited_encoding: str = spec['DelimitedEncoding']
    offsets: List[int] = [int(offset) for offset in spec['Offsets']]
    column_names: List[str] = spec['ColumnNames']
    include_header: bool = spec['IncludeHeader'].lower() == 'true'

    field_positions: List[Tuple[int, int]] = []
    position = 0
    for length in offsets:
        field_positions.append((position, position + length))
        position += length

    # Ensure data directory exists
    os.makedirs(os.path.dirname(output_file), exist_ok=True)

    try:
        with open(input_file, 'r', encoding=encoding) as infile, \
             open(output_file, 'w', encoding=delimited_encoding, newline='') as outfile:
            writer = csv.writer(outfile)
            logging.info(f"Started parsing fixed width file '{input_file}' to CSV '{output_file}'.")

            if include_header:
                header_line = infile.readline()  # Skip header in fixed width file
                writer.writerow(column_names)
            else:
                writer.writerow(column_names)

            # Get total lines for progress bar
            total_lines = sum(1 for _ in infile)
            infile.seek(0)
            if include_header:
                infile.readline()  # Skip header again after seek

            for line in tqdm(infile, total=total_lines, desc="Parsing fixed width records"):
                fields = [line[start:end].strip() for start, end in field_positions]
                writer.writerow(fields)

            logging.info(f"CSV file '{output_file}' generated successfully.")
    except Exception as e:
        logging.error(f"Error parsing fixed width file '{input_file}': {e}")
        raise

if __name__ == '__main__':
    main()
