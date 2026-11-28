
import pytest

from api.app import create_app
from libraryhub.library import Library


@pytest.fixture
def client():
    library = Library()
    app = create_app(library)
    app.config["TESTING"] = True

    with app.test_client() as test_client:
        yield test_client


@pytest.fixture
def sample_book(client):
    response = client.post("/books", json={
        "title": "Software Testing",
        "author": "John Smith",
        "isbn": "1234567890123",
        "total_copies": 3,
    })
    assert response.status_code == 201
    return "1234567890123"


# Positive tests

def test_add_book(client):
    response = client.post("/books", json={
        "title": "Python Basics",
        "author": "Alex",
        "isbn": "1111111111111",
        "total_copies": 2,
    })

    assert response.status_code == 201
    assert response.json["title"] == "Python Basics"
    assert response.json["available_copies"] == 2


def test_get_book(client, sample_book):
    response = client.get(f"/books/{sample_book}")

    assert response.status_code == 200
    assert response.json["isbn"] == sample_book
    assert response.json["title"] == "Software Testing"


def test_borrow_book(client, sample_book):
    response = client.post(
        "/members/101/borrow",
        json={"isbn": sample_book},
    )

    assert response.status_code == 200
    assert response.json["message"] == "Book borrowed successfully"


def test_return_book(client, sample_book):
    client.post("/members/101/borrow", json={"isbn": sample_book})

    response = client.post(
        "/members/101/return",
        json={"isbn": sample_book},
    )

    assert response.status_code == 200
    assert response.json["message"] == "Book returned successfully"


def test_get_fines(client, sample_book):
    client.post("/members/101/borrow", json={"isbn": sample_book})

    response = client.get("/members/101/fines?days_overdue=5")

    assert response.status_code == 200
    assert response.json["fine_tier"] == "Low"


# Negative and boundary tests

def test_unknown_book_returns_404(client):
    response = client.get("/books/9999999999999")

    assert response.status_code == 404
    assert "error" in response.json


def test_borrow_unavailable_book_returns_400(client):
    response = client.post("/books", json={
        "title": "Unavailable Book",
        "author": "Author",
        "isbn": "2222222222222",
        "total_copies": 0,
    })

    assert response.status_code == 201

    response = client.post(
        "/members/101/borrow",
        json={"isbn": "2222222222222"},
    )

    assert response.status_code == 400
    assert "error" in response.json


def test_missing_title_returns_400(client):
    response = client.post("/books", json={
        "author": "Author",
        "isbn": "3333333333333",
        "total_copies": 2,
    })

    assert response.status_code == 400
    assert "error" in response.json


def test_sixth_borrow_returns_400(client):
    isbn = "4444444444444"

    client.post("/books", json={
        "title": "Limit Test",
        "author": "Author",
        "isbn": isbn,
        "total_copies": 6,
    })

    for _ in range(5):
        response = client.post(
            "/members/101/borrow",
            json={"isbn": isbn},
        )
        assert response.status_code == 200

    response = client.post(
        "/members/101/borrow",
        json={"isbn": isbn},
    )

    assert response.status_code == 400
    assert "5 books" in response.json["error"]


# API response schema test

def test_book_response_schema(client, sample_book):
    response = client.get(f"/books/{sample_book}")

    assert response.status_code == 200
    assert set(response.json.keys()) == {
        "title",
        "isbn",
        "author",
        "available_copies",
    }

def test_add_book_invalid_json(client):
    response = client.post("/books", data="invalid json",
                           content_type="application/json")
    assert response.status_code == 400


def test_add_book_invalid_isbn(client):
    response = client.post("/books", json={
        "title": "Test",
        "author": "Author",
        "isbn": "123",
        "total_copies": 2,
    })
    assert response.status_code == 400


def test_add_book_invalid_copies(client):
    response = client.post("/books", json={
        "title": "Test",
        "author": "Author",
        "isbn": "5555555555555",
        "total_copies": -1,
    })
    assert response.status_code == 400


def test_duplicate_book(client, sample_book):
    response = client.post("/books", json={
        "title": "Duplicate",
        "author": "Author",
        "isbn": sample_book,
        "total_copies": 2,
    })
    assert response.status_code == 400


def test_borrow_missing_isbn(client):
    response = client.post("/members/101/borrow", json={})
    assert response.status_code == 400


def test_return_book_not_borrowed(client, sample_book):
    response = client.post(
        "/members/101/return",
        json={"isbn": sample_book},
    )
    assert response.status_code == 400


def test_fines_unknown_member(client):
    response = client.get("/members/999/fines")
    assert response.status_code == 404


def test_fines_negative_days(client, sample_book):
    client.post("/members/101/borrow", json={"isbn": sample_book})
    response = client.get("/members/101/fines?days_overdue=-2")
    assert response.status_code == 400