import sqlite3
from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from sqlalchemy.orm import DeclarativeBase, Mapped, mapped_column
from sqlalchemy import Integer, String, Float

#db = sqlite3.connect("books-collection.db")
#cursor = db.cursor()

#cursor.execute("CREATE TABLE books (id INTEGER PRIMARY KEY, title varchar(250) NOT NULL UNIQUE, author varchar(250) NOT NULL, rating FLOAT NOT NULL)")
#cursor.execute("INSERT INTO books VALUES(1, 'Harry Potter', 'J. K. Rowling', '9.3')")
#db.commit()
class Base(DeclarativeBase):
  pass

db = SQLAlchemy(model_class=Base)

# create the app
app = Flask(__name__)
# configure the SQLite database, relative to the app instance folder
app.config["SQLALCHEMY_DATABASE_URI"] = "sqlite:///new-books-collection.db"
# initialize the app with the extension
db.init_app(app)

class Book(db.Model):
    __tablename__ = 'books'
    id: Mapped[int] = mapped_column(Integer, primary_key=True,nullable=False)
    title: Mapped[str] = mapped_column(String(250), unique=True, nullable=False)
    author: Mapped[str] = mapped_column(nullable=False)
    rating: Mapped[str] = mapped_column(Float, nullable=False)

def add_book():
    book = Book(
        id = 1,
        title = "Harry Potter",
        author = "J.K. Rowling",
        rating = 9
    )
    db.session.add(book)
    db.session.commit()

with app.app_context():
    db.create_all()
    #add_book()

with app.app_context():
    result = db.session.execute(db.select(Book).order_by(Book.title))
    all_books = result.scalars()
    for book in all_books:
        print(book.title)

with app.app_context():
    book = db.session.execute(db.select(Book).where(Book.title == "Harry Potter")).scalar()

with app.app_context():
    book_to_update = db.session.execute(db.select(Book).where(Book.title == "Harry Potter")).scalar()
    book_to_update.title = "Harry Potter and the Chamber of Secrets"
    db.session.commit()

book_id = 1
with app.app_context():
    book_to_update = db.session.execute(db.select(Book).where(Book.id == book_id)).scalar()
    # or book_to_update = db.get_or_404(Book, book_id)
    book_to_update.title = "Harry Potter and the Goblet of Fire"
    db.session.commit()

book_id = 1
with app.app_context():
    book_to_delete = db.session.execute(db.select(Book).where(Book.id == book_id)).scalar()
    # or book_to_delete = db.get_or_404(Book, book_id)
    db.session.delete(book_to_delete)
    db.session.commit()