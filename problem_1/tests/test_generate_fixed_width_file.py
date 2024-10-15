"""Unit tests for generate_fixed_width.py."""

import os
import pytest
from fixed_width_parser.generate_fixed_width_file import generate_fixed_width_file

@pytest.fixture
def spec_file() -> str:
    return 'spec.json'

@pytest.fixture
def output_file() -> str:
    return 'data/test_fixed_width_file.txt'

def test_generate_fixed_width_file(spec_file, output_file) -> None:
    """Test the generation of a fixed width file."""
    num_records = 10

    # Remove output file if it exists
    if os.path.exists(output_file):
        os.remove(output_file)

    generate_fixed_width_file(spec_file, output_file, num_records=num_records)

    assert os.path.exists(output_file)
    with open(output_file, 'r', encoding='windows-1252') as f:
        lines = f.readlines()
        expected_lines = num_records + 1  # Including header
        assert len(lines) == expected_lines
