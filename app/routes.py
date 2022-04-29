
from app import db
from app.models.book import Book
from flask import Blueprint, jsonify,make_response, request

# class Book:
#     def __init__(self, id, title, description):
#         self.id = id
#         self.title = title
#         self.description = description

# books = [
#     Book(1, "Fictional Book", "A fantasy novel set in an imaginary world."),
#     Book(2, "Wheel of Time", "A fantasy novel set in an imaginary world."),
#     Book(3, "Fictional Book Title", "A fantasy novel set in an imaginary world.")
# ]

books_bp = Blueprint("books_bp", __name__, url_prefix="/books")

@books_bp.route("", methods=["GET"])

# def validate_book(book_id):
# #handle invalid book_id, return 400
#     try:
#         book_id = int(book_id)
#     except:
#         return {"message": f"book {book_id} invalid"}, 400 #for invalid inputs
# #search for book_id in data, and return book
#     for book in books:
#         if book.id == book_id:
#             return book

# #return a 404 for non-existing book
#     return {"message": f"book {book_id} not found"}, 404 #not found
def read_all_books():
    if request.method == "GET":
        books = Book.query.all()
        books_response = []
        for book in books:
            books_response.append(
                {
                    "id": book.id,
                    "title": book.title,
                    "description": book.description
                }
            )
        return jsonify(books_response)

@books_bp.route("", methods=["POST"])
def create_book():
    request_body = request.get_json()
    new_book = Book(title = request_body["title"],
                    description = request_body["description"])

    db.session.add(new_book)
    db.session.commit()
    #books.append(new_book) #testing this out in local variable
    return make_response(f"Book {new_book.title} successfully created", 201)