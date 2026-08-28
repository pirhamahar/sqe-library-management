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
};

int main() {
    Library library;

    library.addBook(101);

    // First issue should succeed
    if (!library.issueBook(101)) {
        return 1;
    }

    // Second issue of the same book should fail
    if (library.issueBook(101)) {
        return 1;
    }

    cout << "Already-issued book test passed." << endl;
    return 0;
}
