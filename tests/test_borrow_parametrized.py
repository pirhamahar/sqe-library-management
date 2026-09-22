import pytest
from libraryhub.library import Library


@pytest.mark.parametrize(
    "existing_books, expected_exception",
    [
        (0, None),
        (1, None),
        (2, None),
        (3, None),
        (4, None),
        (5, ValueError),
    ],
    ids=[
        "zero_existing_books",
        "one_existing_book",
        "two_existing_books",
        "three_existing_books",
        "four_existing_books",
        "five_existing_books_limit",
    ],
)
def test_borrow_book_edge_cases(existing_books, expected_exception):
    # Arrange
    library = Library()
    member_id = "M001"

    for i in range(existing_books):
        library.borrow_book(member_id, f"ISBN{i}")

    # Act & Assert
    if expected_exception is None:
        library.borrow_book(member_id, "ISBN_NEW")
        assert len(library.loans[member_id]) == existing_books + 1
    else:
        with pytest.raises(expected_exception):
            library.borrow_book(member_id, "ISBN_NEW")
