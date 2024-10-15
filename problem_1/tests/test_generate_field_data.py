"""Unit tests for generate_field_data function."""

import pytest
from faker import Faker
from fixed_width_parser.generate_fixed_width_file import generate_field_data

@pytest.fixture
def fake() -> Faker:
    return Faker()

def test_generate_field_data_known_fields(fake):
    """Test generate_field_data with known field names."""
    fields = ['f1', 'f2', 'f3', 'f4', 'f5', 'f6', 'f7', 'f8', 'f9', 'f10']
    for field in fields:
        data = generate_field_data(fake, field)
        assert isinstance(data, str)
        assert data.strip() != ''

def test_generate_field_data_unknown_field(fake):
    """Test generate_field_data with an unknown field name."""
    data = generate_field_data(fake, 'unknown_field')
    assert isinstance(data, str)
    assert data.strip() != ''
