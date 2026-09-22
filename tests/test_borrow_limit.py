import pytest
from libraryhub.library import Library


@pytest.fixture
def library():
    # Function scope is the default scope.
    # A fresh Library is created for every test so tests stay independent.
    return Library()


@pytest.fixture(scope="module")
def expensive_library():
    # Module scope creates the fixture once for the whole test module.
    # It is appropriate for expensive setup that can safely be shared
    # by multiple tests.
    return Library()


@pytest.mark.parametrize("current_books", [3])
def test_borrow_book_valid_class(library, current_books):
    for i in range(current_books):
        library.borrow_book("M001", f"ISBN{i}")

    library.borrow_book("M001", "ISBN_NEW")


def test_borrow_book_invalid_class(library):
    for i in range(5):
        library.borrow_book("M001", f"ISBN{i}")

    with pytest.raises(ValueError):
        library.borrow_book("M001", "ISBN6")


@pytest.mark.parametrize("current_books", [4])
def test_borrow_book_boundary_below_limit(library, current_books):
    for i in range(current_books):
        library.borrow_book("M002", f"ISBN{i}")

    library.borrow_book("M002", "ISBN_NEW")


def test_borrow_book_boundary_at_limit(library):
    for i in range(5):
        library.borrow_book("M003", f"ISBN{i}")

    with pytest.raises(ValueError):
        library.borrow_book("M003", "ISBN_NEW")
