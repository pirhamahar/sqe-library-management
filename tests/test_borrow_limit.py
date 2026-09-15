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
