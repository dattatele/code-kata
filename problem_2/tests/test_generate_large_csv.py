"""Tests for generate_large_csv.py."""

import os
import pytest
from data_processing.generate_large_csv import generate_large_csv, main


def test_generate_large_csv_valid():
    """Test generating a CSV file with valid parameters."""
    input_file = os.path.join('data', 'test_large_input.csv')
    target_size_gb = 0.0001  # Small size for testing purposes (~100 KB)

    generate_large_csv(input_file, target_size_gb)

    assert os.path.exists(input_file)
    current_size = os.path.getsize(input_file)
    target_size_bytes = target_size_gb * 1024 * 1024 * 1024
    assert current_size >= target_size_bytes

    # Clean up
    os.remove(input_file)


def test_generate_large_csv_invalid_size():
    """Test generating a CSV file with invalid target size."""
    input_file = os.path.join('data', 'test_large_input.csv')
    target_size_gb = -1  # Invalid size

    with pytest.raises(ValueError) as exc_info:
        generate_large_csv(input_file, target_size_gb)

    assert "Target size must be positive and greater than zero." in str(exc_info.value)


def test_generate_large_csv_io_error(monkeypatch):
    """Test handling of IOError during file operations."""

    def mock_open(*args, **kwargs):
        raise IOError("Mocked IOError")

    monkeypatch.setattr('builtins.open', mock_open)

    input_file = os.path.join('data', 'test_large_input.csv')
    target_size_gb = 0.0001

    with pytest.raises(IOError) as exc_info:
        generate_large_csv(input_file, target_size_gb)

    assert "Mocked IOError" in str(exc_info.value)


def test_generate_large_csv_main():
    """Test the main function with a small target size."""
    # Override the target size for testing
    def mock_main(target_size_gb=None):
        main(target_size_gb=0.0001)

    # Run the mocked main function
    mock_main()

    # Verify the file was created
    output_file = os.path.join('data', 'large_input.csv')
    assert os.path.exists(output_file)

    # Clean up
    os.remove(output_file)
