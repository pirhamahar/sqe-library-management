
def fine_tier(days_overdue):
    if days_overdue < 0:
        raise ValueError("Days overdue cannot be negative")
    elif days_overdue == 0:
        return "None"
    elif 1 <= days_overdue <= 7:
        return "Low"
    elif 8 <= days_overdue <= 14:
        return "Medium"
    elif 15 <= days_overdue <= 30:
        return "High"
    else:
        return "Severe"


class LibraryIOError(Exception):
    """Custom exception for library file I/O errors."""
    pass


class Library:
    def __init__(self):
        self.loans = {}
        self.catalog = {}

    def add_book(self, isbn, total_copies):
        self.catalog[isbn] = total_copies

    def total_available_copies(self):
        return sum(self.catalog.values())

    def borrow_book(self, member_id, isbn):
        current_books = self.loans.get(member_id, [])

        if len(current_books) >= 5:
            raise ValueError("Member cannot borrow more than 5 books")

        current_books.append(isbn)
        self.loans[member_id] = current_books

    def export_catalog(self, path):
        content = ""

        for isbn, total_copies in self.catalog.items():
            content += f"{isbn},{total_copies}\n"

        try:
            with open(path, "w") as file:
                file.write(content)
        except OSError as error:
            raise LibraryIOError(
                f"Unable to export catalog: {path}"
            ) from error


def validate_isbn(isbn):
    if not isinstance(isbn, str):
        raise ValueError("ISBN must be a string")

    if len(isbn) != 13:
        raise ValueError("ISBN must contain exactly 13 digits")

    if not isbn.isdigit():
        raise ValueError("ISBN must contain only numeric digits")

    return True


def borrow_percentile(member, library):
    """
    Calculate the percentile rank of a member based on loan records.

    Raises:
        ValueError: If the library is empty or the member does not exist.

    Returns:
        float: A percentile rank between 0.0 and 100.0.
               A single-member library returns 100.0.
    """
    members = list(library.loans.keys())

    if not members:
        raise ValueError("Cannot calculate percentile for an empty library")

    if member not in members:
        raise ValueError("Member does not exist in the library")

    if len(members) == 1:
        return 100.0

    rank_index = members.index(member)

    return rank_index / (len(members) - 1) * 100.0
