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
