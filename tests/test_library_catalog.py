import pytest
from libraryhub.library import Library


@pytest.fixture
def empty_library():
    # Arrange
    return Library()


@pytest.fixture
def populated_library():
    # Arrange
    library = Library()
    library.add_book("ISBN001", 2)
    library.add_book("ISBN002", 3)
    return library


def test_total_available_copies_empty_catalog(empty_library):
    # Act
    result = empty_library.total_available_copies()

    # Assert
    assert result == 0


def test_total_available_copies_single_book(empty_library):
    # Arrange
    empty_library.add_book("ISBN001", 5)

    # Act
    result = empty_library.total_available_copies()

    # Assert
    assert result == 5


def test_total_available_copies_multiple_books(populated_library):
    # Act
    result = populated_library.total_available_copies()

    # Assert
    assert result == 5
