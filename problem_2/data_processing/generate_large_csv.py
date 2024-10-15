"""Efficiently generate a large CSV file with personal information."""

import os
import csv
import random
from typing import List, Optional


def generate_large_csv(output_file: str, target_size_gb: float) -> None:
    """Generate a large CSV file with synthetic personal data.

    Args:
        output_file (str): Path to the output CSV file.
        target_size_gb (float): Target file size in gigabytes.

    Raises:
        ValueError: If the target_size_gb is not positive.
        IOError: If there is an issue writing to the output file.
    """
    if target_size_gb <= 0:
        raise ValueError("Target size must be positive and greater than zero.")

    fieldnames: List[str] = ['first_name', 'last_name', 'address', 'date_of_birth']
    os.makedirs(os.path.dirname(output_file), exist_ok=True)

    target_size_bytes = target_size_gb * 1024 * 1024 * 1024  # Convert GB to bytes
    current_size = 0
    record_count = 0

    first_names = ['John', 'Jane', 'Alice', 'Bob', 'Carol', 'Dave', 'Eve', 'Frank']
    last_names = ['Smith', 'Doe', 'Johnson', 'Williams', 'Brown', 'Jones', 'Miller']
    streets = ['Main St', 'High St', 'Pearl St', 'Maple Ave', 'Park Ave', 'Cedar St']
    cities = ['Springfield', 'Riverside', 'Greenville', 'Centerville', 'Fairview']
    states = ['CA', 'NY', 'TX', 'FL', 'IL']
    date_of_births = ['1990-01-01', '1985-05-15', '1970-07-20', '2000-12-31']

    try:
        with open(output_file, 'w', newline='', encoding='utf-8') as csvfile:
            writer = csv.DictWriter(csvfile, fieldnames=fieldnames)
            writer.writeheader()

            while current_size < target_size_bytes:
                row = {
                    'first_name': random.choice(first_names),
                    'last_name': random.choice(last_names),
                    'address': f"{random.randint(100, 9999)} {random.choice(streets)}, {random.choice(cities)}, {random.choice(states)}",
                    'date_of_birth': random.choice(date_of_births)
                }
                writer.writerow(row)
                record_count += 1

                # Update current file size after every 10,000 records to improve performance
                if record_count % 10000 == 0:
                    csvfile.flush()
                    os.fsync(csvfile.fileno())
                    current_size = os.path.getsize(output_file)
                    # Optional: Print progress
                    print(f"Generated {record_count} records. Current file size: {current_size / (1024 ** 3):.2f} GB", end='\r')

        print(f"\nGenerated {record_count} records in '{output_file}' with size {current_size / (1024 ** 3):.2f} GB")
    except IOError as e:
        print(f"Error writing to file '{output_file}': {e}")
        raise e


def main(target_size_gb: Optional[float] = None) -> None:
    """Main function to generate the large CSV file.

    Args:
        target_size_gb (Optional[float]): Target file size in GB. If None, defaults to 2.0 GB.
    """
    if target_size_gb is None:
        target_size_gb = 2.0  # Default to 2 GB if not specified

    output_file = os.path.join('data', 'large_input.csv')
    print(f"Generating large CSV file of approximately {target_size_gb} GB...")
    try:
        generate_large_csv(output_file, target_size_gb)
    except Exception as e:
        print(f"An error occurred during CSV generation: {e}")


if __name__ == '__main__':
    main()
