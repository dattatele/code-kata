"""Unit tests for parse_fixed_width.py."""

import os
import csv
import pytest
from fixed_width_parser.generate_fixed_width_file import generate_fixed_width_file
from fixed_width_parser.parse_fixed_width_file import parse_fixed_width_file

@pytest.fixture
def spec_file() -> str:
    return 'spec.json'

@pytest.fixture
def fixed_width_file() -> str:
    return 'data/test_fixed_width_file.txt'

@pytest.fixture
def output_csv_file() -> str:
    return 'data/test_output.csv'

def test_parse_fixed_width_file(spec_file, fixed_width_file, output_csv_file) -> None:
    """Test the parsing of a fixed width file into CSV."""
    num_records = 10

    # Remove output files if they exist
    if os.path.exists(fixed_width_file):
        os.remove(fixed_width_file)
    if os.path.exists(output_csv_file):
        os.remove(output_csv_file)

    # Generate a fixed width file to parse
    generate_fixed_width_file(spec_file, fixed_width_file, num_records=num_records)

    # Parse the fixed width file
    parse_fixed_width_file(spec_file, fixed_width_file, output_csv_file)

    assert os.path.exists(output_csv_file)
    with open(output_csv_file, 'r', encoding='utf-8') as f:
        reader = csv.DictReader(f)
        rows = list(reader)
        expected_rows = num_records
        assert len(rows) == expected_rows
        # Verify that the data is correctly parsed
        for row in rows:
            assert all(value.strip() != '' for value in row.values())
