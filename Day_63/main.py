from flask import Flask, render_template, request, redirect, url_for
from flask_sqlalchemy import SQLAlchemy
from sqlalchemy.orm import DeclarativeBase, Mapped, mapped_column
from sqlalchemy import Integer, String, Float

'''
Red underlines? Install the required packages first: 
Open the Terminal in PyCharm (bottom left). 

On Windows type:
python -m pip install -r requirements.txt

On MacOS type:
pip3 install -r requirements.txt

This will install the packages from requirements.txt for this project.
'''
class Base(DeclarativeBase):
  pass

db = SQLAlchemy(model_class=Base)

app = Flask(__name__)
app.config["SQLALCHEMY_DATABASE_URI"] = "sqlite:///new-books-collection.db"
db.init_app(app)

all_books = []

class Book(db.Model):
    __tablename__ = 'books'
    id: Mapped[int] = mapped_column(Integer, primary_key=True,nullable=False)
    title: Mapped[str] = mapped_column(String(250), unique=True, nullable=False)
    author: Mapped[str] = mapped_column(nullable=False)
    rating: Mapped[str] = mapped_column(Float, nullable=False)

@app.route('/')
def home():
    with app.app_context():
        result = db.session.execute(db.select(Book).order_by(Book.title))
        all_books = result.scalars().all()
    return render_template('index.html', all_books=all_books)


@app.route("/add", methods=["POST","GET"])
def add():
    if request.method == "GET":
        return render_template('add.html')
    elif request.method == "POST":
        name = request.form["name"]
        author = request.form["author"]
        rating = request.form["rating"]
        book = Book(
            title = name,
            author = author,
            rating = float(rating)
        )
        with app.app_context():
            db.session.add(book)
            db.session.commit()
        return redirect(url_for('home'))
    return render_template('add.html')

@app.route("/edit/<int:index>", methods=["POST","GET"])
def edit(index):
    with app.app_context():
        book_to_update = db.session.execute(db.select(Book).where(Book.id == index)).scalar()
        if request.method == "GET":
            return render_template("edit.html", book=book_to_update)
        elif request.method == "POST":
            rating = request.form["rating"]
            book_to_update.rating = float(rating)
            print(rating)
            db.session.commit()
            return redirect(url_for('home'))

@app.route("/delete/<int:index>", methods=["GET"])
def delete(index):
    with app.app_context():
        book_to_delete = db.session.execute(db.select(Book).where(Book.id == index)).scalar()
        if request.method == "GET":
            db.session.delete(book_to_delete)
            db.session.commit()
            return redirect(url_for('home'))

if __name__ == "__main__":
    app.run(debug=True)

