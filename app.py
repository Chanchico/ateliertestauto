# EXERCICE 5-1

from flask import Flask, request, jsonify
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///books.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
db = SQLAlchemy(app)

class Book(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(80), nullable=False)
    author = db.Column(db.String(80), nullable=False)
    isbn = db.Column(db.String(20), unique=True, nullable=False)
    description = db.Column(db.String(200), nullable=True)

    def as_dict(self):
        return {c.name: getattr(self, c.name) for c in self.__table__.columns}

@app.route('/books', methods=['GET'])
def get_books():
    books = Book.query.all()
    return jsonify([book.as_dict() for book in books])

@app.route('/book/<int:id>', methods=['GET'])
def get_book(id):
    book = Book.query.get_or_404(id)
    return jsonify(book.as_dict())

@app.route('/book', methods=['POST'])
def create_book():
    data = request.get_json()
    new_book = Book(
        title=data['title'],
        author=data['author'],
        isbn=data['isbn'],
        description=data.get('description')
    )
    db.session.add(new_book)
    db.session.commit()
    return jsonify(new_book.as_dict()), 201

@app.route('/book/<int:id>', methods=['PUT'])
def update_book(id):
    data = request.get_json()
    book = Book.query.get_or_404(id)
    book.title = data['title']
    book.author = data['author']
    book.isbn = data['isbn']
    book.description = data.get('description')
    db.session.commit()
    return jsonify(book.as_dict())

@app.route('/book/<int:id>', methods=['DELETE'])
def delete_book(id):
    book = Book.query.get_or_404(id)
    db.session.delete(book)
    db.session.commit()
    return '', 204

def setup_db():
    with app.app_context():
        db.create_all()

if __name__ == '__main__':
    setup_db()
    app.run(debug=True)
