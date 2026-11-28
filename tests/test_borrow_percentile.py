import pytest

from libraryhub.library import Library, borrow_percentile


def test_borrow_percentile_normal_case():
    library = Library()
    library.borrow_book("member1", "ISBN001")
    library.borrow_book("member2", "ISBN002")
    library.borrow_book("member3", "ISBN003")

    assert borrow_percentile("member1", library) == 0.0
    assert borrow_percentile("member2", library) == 50.0
    assert borrow_percentile("member3", library) == 100.0


def test_borrow_percentile_one_member():
    library = Library()
    library.borrow_book("member1", "ISBN001")

    assert borrow_percentile("member1", library) == 100.0


def test_borrow_percentile_empty_library():
    library = Library()

    with pytest.raises(ValueError):
        borrow_percentile("member1", library)


def test_borrow_percentile_unknown_member():
    library = Library()
    library.borrow_book("member1", "ISBN001")

    with pytest.raises(ValueError):
        borrow_percentile("member2", library)