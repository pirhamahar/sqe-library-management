import pytest
from libraryhub.library import validate_isbn

def test_valid_isbn():
    assert validate_isbn("9781234567890") is True

@pytest.mark.parametrize("isbn", [
    "",
    "978123456789",
    "978123456789A",
    "978-1234567890"
])
def test_invalid_isbn_classes(isbn):
    with pytest.raises(ValueError):
        validate_isbn(isbn)

@pytest.mark.parametrize("length", [11, 12, 14, 15])
def test_validate_isbn_length_boundaries_invalid(length):
    isbn = "1" * length

    with pytest.raises(ValueError):
        validate_isbn(isbn)


def test_validate_isbn_length_boundary_valid():
    isbn = "1" * 13

    assert validate_isbn(isbn) is True
