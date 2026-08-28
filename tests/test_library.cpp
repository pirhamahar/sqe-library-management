#include <iostream>
#include <vector>
using namespace std;

class Book {
public:
    int bookId;
    bool issued;

    Book(int id) {
        bookId = id;
        issued = false;
    }
};

class Library {
private:
    vector<Book> books;

public:
    void addBook(int bookId) {
        books.push_back(Book(bookId));
    }

    bool issueBook(int bookId) {
        for (Book &book : books) {
            if (book.bookId == bookId) {
                if (book.issued) {
                    return false;
                }

                book.issued = true;
                return true;
            }
        }

        return false;
    }

    bool returnBook(int bookId) {
        for (Book &book : books) {
            if (book.bookId == bookId) {
                if (!book.issued) {
                    return false;
                }

                book.issued = false;
                return true;
            }
        }

        return false;
    }

    bool isAvailable(int bookId) {
        for (Book &book : books) {
            if (book.bookId == bookId) {
                return !book.issued;
            }
        }

        return false;
    }
};

int main() {
    Library library;

    library.addBook(101);

    // New book should be available
    if (!library.isAvailable(101)) {
        return 1;
    }

    // After issuing, book should not be available
    if (!library.issueBook(101)) {
        return 1;
    }

    if (library.isAvailable(101)) {
        return 1;
    }

    // After returning, book should become available again
    if (!library.returnBook(101)) {
        return 1;
    }

    if (!library.isAvailable(101)) {
        return 1;
    }

    cout << "Book availability status test passed." << endl;
    return 0;
}
