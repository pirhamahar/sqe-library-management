import pytest
from libraryhub.library import Library

@pytest.mark.parametrize('current_books', [3])
def test_borrow_book_valid_class(current_books):
    library = Library()

    for i in range(current_books):
        library.borrow_book("M001", f"ISBN{i}")

    library.borrow_book("M001", "ISBN_NEW")


def test_borrow_book_invalid_class():
    library = Library()

    for i in range(5):
        library.borrow_book("M001", f"ISBN{i}")

    with pytest.raises(ValueError):
        library.borrow_book("M001", "ISBN6")

@pytest.mark.parametrize("current_books", [4])
def test_borrow_book_boundary_below_limit(current_books):
    library = Library()

    for i in range(current_books):
        library.borrow_book("M002", f"ISBN{i}")

    library.borrow_book("M002", "ISBN_NEW")


def test_borrow_book_boundary_at_limit():
    library = Library()

    for i in range(5):
        library.borrow_book("M003", f"ISBN{i}")

    with pytest.raises(ValueError):
        library.borrow_book("M003", "ISBN_NEW")
