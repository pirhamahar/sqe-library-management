class Library:
    def __init__(self):
        self.loans = {}

    def borrow_book(self, member_id, isbn):
        current_books = self.loans.get(member_id, [])

        if len(current_books) >= 5:
            raise ValueError("Member cannot borrow more than 5 books")

        current_books.append(isbn)
        self.loans[member_id] = current_books
