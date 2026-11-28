
# Lab 12: API Exploration — LibraryHub

## Objective
Explore the LibraryHub REST API and verify HTTP status codes, response payloads, and error handling.

## Tools Used
- Python 3.11
- Flask
- Postman / PowerShell
- Pytest

## Starting the API

Run the following commands from the project root:

```powershell
$env:PYTHONPATH = "src"
py -3.11 -m api.app
```

The API runs at:

`http://127.0.0.1:5000`

## 1. POST /books — Add a Book

Request:
```json
{
  "title": "Software Testing",
  "author": "John Smith",
  "isbn": "1234567890123",
  "total_copies": 3
}
```

Expected status: `201 Created`

Expected response:
```json
{
  "title": "Software Testing",
  "isbn": "1234567890123",
  "author": "John Smith",
  "available_copies": 3
}
```

## 2. GET /books/<isbn> — Retrieve a Book

Request:

`GET http://127.0.0.1:5000/books/1234567890123`

Expected status: `200 OK`

Expected response: Book details containing title, ISBN, author, and available copies.

## 3. POST /members/<member_id>/borrow — Borrow a Book

Request:
```json
{
  "isbn": "1234567890123"
}
```

Expected status: `200 OK`

Expected response:
```json
{
  "message": "Book borrowed successfully",
  "member_id": "101",
  "isbn": "1234567890123"
}
```

## 4. POST /members/<member_id>/return — Return a Book

Request:
```json
{
  "isbn": "1234567890123"
}
```

Expected status: `200 OK`

Expected response: Confirmation that the book was returned successfully.

## 5. GET /members/<member_id>/fines — Retrieve Fine Information

Request:

`GET http://127.0.0.1:5000/members/101/fines?days_overdue=5`

Expected status: `200 OK`

Expected response:
```json
{
  "member_id": "101",
  "days_overdue": 5,
  "fine_tier": "Low"
}
```

## Negative and Boundary Testing

### Test 1: Unknown ISBN

Request:

`GET /books/9999999999999`

Expected status: `404 Not Found`

Expected response:
```json
{
  "error": "Book not found"
}
```

### Test 2: Missing Book Title

Request:
```json
{
  "author": "Author",
  "isbn": "3333333333333",
  "total_copies": 2
}
```

Expected status: `400 Bad Request`

Expected response:
```json
{
  "error": "Missing required book fields"
}
```

### Additional Boundary Test: Borrowing Limit

A member can borrow a maximum of five books. An attempt to borrow a sixth book should return:

`400 Bad Request`

## HTTP Status Code Summary

| Status Code | Meaning | API Scenario |
|---|---|---|
| 200 | OK | Successful GET, borrow, and return |
| 201 | Created | Book successfully added |
| 400 | Bad Request | Invalid or incomplete request |
| 404 | Not Found | Unknown book or member |

## Conclusion

The LibraryHub REST API provides endpoints for adding and retrieving books, borrowing and returning books, and retrieving member fine information.

Positive, negative, and boundary test cases were implemented using Pytest and Flask's test client. The complete project test suite passed 68 tests with an overall coverage of 92.96%.
