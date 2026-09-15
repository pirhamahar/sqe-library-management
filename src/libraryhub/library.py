def fine_tier(days_overdue):
    if days_overdue < 0:
        raise ValueError("Days overdue cannot be negative")
    elif days_overdue == 0:
        return "None"
    elif 1 <= days_overdue <= 7:
        return "Low"
    elif 8 <= days_overdue <= 14:
        return "Medium"
    elif 15 <= days_overdue < 30:
        return "High"
    else:
        return "Severe"

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
