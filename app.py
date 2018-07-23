from flask import Flask, jsonify, request
from test import validateBook

app = Flask(__name__)
print(__name__)

books = [
    {
        'name': 'Book 1',
        'price': 9.95,
        'isbn': 123456,
    },
    {
        'name': 'Book 2',
        'price': 14.95,
        'isbn': 654321,
    }
]

# 
# GET routes
# 

@app.route('/')
def home():
    return 'This is the homepage <a href="/books">Go to books</a>'

@app.route('/books')
def get_books():
    return jsonify({'books': books})

@app.route('/books', methods=['POST'])
def add_book():
    # return jsonify(request.get_json())
    request_data = request.get_json()
    if (validateBook(request_data)):
        new_book = {
            "name": request_data['name'],
            "price": request_data['price'],
            "isbn": request_data['isbn']
        }
        books.insert(0, new_book)
        # books.append(request_data)
        return "True"
    else:
        return "False"

    # return validateBook(jsonify(request.get_json()))

@app.route('/books/<int:isbn>')
def get_book_by_isbn(isbn):
    return_value = {}
    for book in books:
        if book['isbn'] == isbn:
            return_value = {
                'name': book['name'],
                'price': book['price']
            }

    return jsonify(return_value)

app.run(port=5000, debug=True)