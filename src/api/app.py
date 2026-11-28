
from flask import Flask, jsonify, request

from libraryhub.library import Library, fine_tier, validate_isbn


def create_app(library=None):
    app = Flask(__name__)

    library = library or Library()
    book_details = {}
    members = set()

    @app.route("/books", methods=["POST"])
    def add_book():
        data = request.get_json(silent=True)

        if not isinstance(data, dict):
            return jsonify({"error": "A valid JSON object is required"}), 400

        required = ["title", "author", "isbn", "total_copies"]
        if any(field not in data for field in required):
            return jsonify({"error": "Missing required book fields"}), 400

        title = data["title"]
        author = data["author"]
        isbn = data["isbn"]
        copies = data["total_copies"]

        if not isinstance(title, str) or not title.strip():
            return jsonify({"error": "Title must be a non-empty string"}), 400

        if not isinstance(author, str) or not author.strip():
            return jsonify({"error": "Author must be a non-empty string"}), 400

        try:
            validate_isbn(isbn)
        except ValueError as error:
            return jsonify({"error": str(error)}), 400

        if isinstance(copies, bool) or not isinstance(copies, int) or copies < 0:
            return jsonify({"error": "total_copies must be a non-negative integer"}), 400

        if isbn in book_details:
            return jsonify({"error": "Book already exists"}), 400

        library.add_book(isbn, copies)
        book_details[isbn] = {
            "title": title.strip(),
            "isbn": isbn,
            "author": author.strip(),
            "available_copies": copies,
        }

        return jsonify(book_details[isbn]), 201

    @app.route("/books/<isbn>", methods=["GET"])
    def get_book(isbn):
        book = book_details.get(isbn)

        if book is None:
            return jsonify({"error": "Book not found"}), 404

        return jsonify(book), 200

    @app.route("/members/<member_id>/borrow", methods=["POST"])
    def borrow_book(member_id):
        data = request.get_json(silent=True)

        if not isinstance(data, dict) or not isinstance(data.get("isbn"), str):
            return jsonify({"error": "A valid ISBN is required"}), 400

        isbn = data["isbn"]
        book = book_details.get(isbn)

        if book is None:
            return jsonify({"error": "Book not found"}), 404

        if book["available_copies"] <= 0:
            return jsonify({"error": "No available copies"}), 400

        try:
            library.borrow_book(member_id, isbn)
        except ValueError as error:
            return jsonify({"error": str(error)}), 400

        book["available_copies"] -= 1
        members.add(member_id)

        return jsonify({
            "message": "Book borrowed successfully",
            "member_id": member_id,
            "isbn": isbn,
        }), 200

    @app.route("/members/<member_id>/return", methods=["POST"])
    def return_book(member_id):
        data = request.get_json(silent=True)

        if not isinstance(data, dict) or not isinstance(data.get("isbn"), str):
            return jsonify({"error": "A valid ISBN is required"}), 400

        isbn = data["isbn"]
        book = book_details.get(isbn)

        if book is None:
            return jsonify({"error": "Book not found"}), 404

        borrowed_books = library.loans.get(member_id, [])

        if isbn not in borrowed_books:
            return jsonify({"error": "Member has not borrowed this book"}), 400

        borrowed_books.remove(isbn)
        book["available_copies"] += 1

        return jsonify({
            "message": "Book returned successfully",
            "member_id": member_id,
            "isbn": isbn,
        }), 200

    @app.route("/members/<member_id>/fines", methods=["GET"])
    def get_fines(member_id):
        if member_id not in members:
            return jsonify({"error": "Member not found"}), 404

        days_value = request.args.get("days_overdue", default="0")

        try:
            days_overdue = int(days_value)
            tier = fine_tier(days_overdue)
        except (ValueError, TypeError):
            return jsonify({"error": "days_overdue must be a non-negative integer"}), 400

        return jsonify({
            "member_id": member_id,
            "days_overdue": days_overdue,
            "fine_tier": tier,
        }), 200

    return app


app = create_app()


if __name__ == "__main__":
    app.run(debug=True)
