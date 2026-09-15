class Library:
    def __init__(self):
        self.loans = {}

    def borrow_book(self, member_id, isbn):
        current_books = self.loans.get(member_id, [])

        if len(current_books) >= 5:
            raise ValueError("Member cannot borrow more than 5 books")

        current_books.append(isbn)
        self.loans[member_id] = current_books

def validate_isbn(isbn):
    if not isinstance(isbn, str):
        raise ValueError("ISBN must be a string")

    if len(isbn) != 13:
        raise ValueError("ISBN must contain exactly 13 digits")

    if not isbn.isdigit():
        raise ValueError("ISBN must contain only numeric digits")

    return True
