"""Tests for anonymize_data.py."""

import os
import pytest
import shutil
from data_processing.anonymize_data import anonymize_data, main
from data_processing.generate_large_csv import generate_large_csv


def test_anonymize_data_valid():
    """Test anonymizing data with valid input."""
    input_file = os.path.join('data', 'test_large_input.csv')
    output_dir = os.path.join('data', 'test_anonymized_output')
    target_size_gb = 0.0001  # Small size for testing purposes

    # Generate test input data
    generate_large_csv(input_file, target_size_gb)

    # Anonymize data
    columns_to_anonymize = ['first_name', 'last_name', 'address']
    anonymize_data(input_file, output_dir, columns_to_anonymize)

    # Check that the output directory exists
    assert os.path.exists(output_dir)
    output_files = os.listdir(output_dir)
    csv_files = [file for file in output_files if file.startswith('part-') and file.endswith('.csv')]
    assert len(csv_files) > 0

    # Clean up
    shutil.rmtree(output_dir)
    os.remove(input_file)


def test_anonymize_data_missing_file():
    """Test anonymizing data when input file does not exist."""
    input_file = os.path.join('data', 'non_existent_file.csv')
    output_dir = os.path.join('data', 'test_anonymized_output')
    columns_to_anonymize = ['first_name', 'last_name', 'address']

    with pytest.raises(FileNotFoundError) as exc_info:
        anonymize_data(input_file, output_dir, columns_to_anonymize)

    assert f"Input file '{input_file}' does not exist." in str(exc_info.value)


def test_anonymize_data_no_columns():
    """Test anonymizing data with no columns specified."""
    input_file = os.path.join('data', 'test_large_input.csv')
    output_dir = os.path.join('data', 'test_anonymized_output')
    target_size_gb = 0.0001

    # Generate test input data
    generate_large_csv(input_file, target_size_gb)

    columns_to_anonymize = []

    with pytest.raises(ValueError) as exc_info:
        anonymize_data(input_file, output_dir, columns_to_anonymize)

    assert "No columns specified for anonymization." in str(exc_info.value)

    # Clean up
    os.remove(input_file)


def test_anonymize_data_invalid_column():
    """Test anonymizing data with an invalid column name."""
    input_file = os.path.join('data', 'test_large_input.csv')
    output_dir = os.path.join('data', 'test_anonymized_output')
    target_size_gb = 0.0001

    # Generate test input data
    generate_large_csv(input_file, target_size_gb)

    columns_to_anonymize = ['non_existent_column']

    with pytest.raises(ValueError) as exc_info:
        anonymize_data(input_file, output_dir, columns_to_anonymize)

    assert "Column 'non_existent_column' not found in input data." in str(exc_info.value)

    # Clean up
    os.remove(input_file)


def test_anonymize_data_main():
    """Test the main function of anonymize_data.py."""
    # Generate input data
    input_file = os.path.join('data', 'large_input.csv')
    target_size_gb = 0.0001
    generate_large_csv(input_file, target_size_gb)

    # Run the main function
    main()

    # Verify the output directory exists
    output_dir = os.path.join('data', 'anonymized_output')
    assert os.path.exists(output_dir)

    # Clean up
    shutil.rmtree(output_dir)
    os.remove(input_file)
