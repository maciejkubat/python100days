from flask import Flask, render_template, redirect, url_for, request
from flask_bootstrap import Bootstrap5
from flask_sqlalchemy import SQLAlchemy
from sqlalchemy.orm import DeclarativeBase, Mapped, mapped_column
from sqlalchemy import Integer, String, Float
from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField
from wtforms.validators import DataRequired
import requests
import os

TMDB_TOKEN = os.environ.get("TMDB_TOKEN")

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
app.config['SECRET_KEY'] = '8BYkEfBA6O6donzWlSihBXox7C0sKR6b'
Bootstrap5(app)

app.config["SQLALCHEMY_DATABASE_URI"] = "sqlite:///movie-list.db"
db.init_app(app)

# CREATE DB
class Movie(db.Model):
    __tablename__ = 'movie'
    id: Mapped[int] = mapped_column(Integer, primary_key=True,nullable=False)
    title: Mapped[str] = mapped_column(String(250), unique=True, nullable=False)
    year: Mapped[int] = mapped_column(Integer, nullable=False)
    description: Mapped[str] = mapped_column(String(500), nullable=False)
    rating: Mapped[str] = mapped_column(Float, nullable=True)
    ranking: Mapped[int] = mapped_column(Integer, nullable=True)
    review: Mapped[str] = mapped_column(String(250), nullable=True)
    img_url: Mapped[str] = mapped_column(String(500), nullable=False)

class EditForm(FlaskForm):
    rating = StringField('Your rating', validators=[DataRequired()])
    review = StringField('Your review', validators=[DataRequired()])
    submit = SubmitField('Done')

class AddForm(FlaskForm):
    title = StringField('Movie Title', validators=[DataRequired()])
    submit = SubmitField('Add Movie')

# CREATE TABLE
def add_entry():
    new_movie = Movie(
        title="Phone Booth",
        year=2002,
        description="Publicist Stuart Shepard finds himself trapped in a phone booth, pinned down by an extortionist's sniper rifle. Unable to leave or receive outside help, Stuart's negotiation with the caller leads to a jaw-dropping climax.",
        rating=7.3,
        ranking=10,
        review="My favourite character was the caller.",
        img_url="https://image.tmdb.org/t/p/w500/tjrX2oWRCM3Tvarz38zlZM7Uc10.jpg"
    )
    second_movie = Movie(
        title="Avatar The Way of Water",
        year=2022,
        description="Set more than a decade after the events of the first film, learn the story of the Sully family (Jake, Neytiri, and their kids), the trouble that follows them, the lengths they go to keep each other safe, the battles they fight to stay alive, and the tragedies they endure.",
        rating=7.3,
        ranking=9,
        review="I liked the water.",
        img_url="https://image.tmdb.org/t/p/w500/t6HIqrRAclMCA60NsSmeqe9RmNV.jpg"
    )
    with app.app_context():
        db.session.add(new_movie)
        db.session.add(second_movie)
        db.session.commit()

@app.route("/edit/<int:index>", methods=["GET", "POST"])
def edit(index):
    form = EditForm()
    with app.app_context():
        movie_to_update = db.session.execute(db.select(Movie).where(Movie.id == index)).scalar()
        if request.method == "GET":
            return render_template("edit.html", movie=movie_to_update, form=form)
        elif request.method == "POST" and form.validate_on_submit():
            rating = form.rating.data
            review = form.review.data
            movie_to_update.rating = float(rating)
            movie_to_update.review = review
            db.session.commit()
            return redirect(url_for('home'))
    return render_template("edit.html", movie=movie_to_update, form=form)

@app.route("/delete/<int:index>", methods=["GET"])
def delete(index):
    with app.app_context():
        movie_to_delete = db.session.execute(db.select(Movie).where(Movie.id == index)).scalar()
        if request.method == "GET":
            db.session.delete(movie_to_delete)
            db.session.commit()
            return redirect(url_for('home'))

@app.route("/add", methods=["GET","POST"])
def add():
    form = AddForm()
    if request.method == "GET":
        return render_template("add.html",form=form)
    elif request.method == "POST" and form.validate_on_submit():
        title = form.title.data
        movies = get_movies(title)
        return render_template("select.html",movies=movies)

@app.route( "/add_to_list/<int:index>")
def add_to_list(index):
    url = f"https://api.themoviedb.org/3/movie/{index}"
    parameters = {
        "language" : "en-US"
    }
    headers = {
        "accept": "application/json",
        "Authorization": f"Bearer {TMDB_TOKEN}"
    }
    response = requests.get(url, headers=headers, params=parameters)
    response.raise_for_status()
    data = response.json()
    print(data)
    new_movie = Movie(
        title=data['title'],
        year=data['release_date'].split("-")[0],
        description=data['overview'],
        img_url=f"https://image.tmdb.org/t/p/w500{data['poster_path']}"
    )
    with app.app_context():
        db.session.add(new_movie)
        db.session.commit()
        movie_to_update = db.session.execute(db.select(Movie).where(Movie.title == new_movie.title)).scalar()
        db.session.commit()
        return redirect(url_for('edit',index=movie_to_update.id))

def get_movies(title):
    parameters = {
        "query" : title,
        "include_adult" : "false",
        "language" : "en-US",
        "page" : 1
    }
    url = "https://api.themoviedb.org/3/search/movie"
    headers = {
        "accept": "application/json",
        "Authorization": f"Bearer {TMDB_TOKEN}"
    }
    response = requests.get(url, headers=headers, params=parameters)
    response.raise_for_status()
    data = response.json()["results"]
    return data


@app.route("/")
def home():
    with app.app_context():
        result = db.session.execute(db.select(Movie).order_by(Movie.rating))
        all_movies = result.scalars().all()
        for index,movie in enumerate(reversed(all_movies)):
            movie.ranking = index + 1
    return render_template("index.html", all_movies=all_movies)

# with app.app_context():
#     db.create_all()
#     add_entry()

# with app.app_context():
#     result = db.session.execute(db.select(Movie).order_by(Movie.title))
#     all_books = result.scalars()
#     for book in all_books:
#         print(book.title)

if __name__ == '__main__':
   app.run(debug=True)
