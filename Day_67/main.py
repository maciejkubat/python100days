
from flask import Flask, render_template, redirect, url_for, request
from flask_bootstrap import Bootstrap5
from flask_sqlalchemy import SQLAlchemy
from sqlalchemy.orm import DeclarativeBase, Mapped, mapped_column
from sqlalchemy import Integer, String, Text
from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField
from wtforms.validators import DataRequired, URL
from flask_ckeditor import CKEditor, CKEditorField
from datetime import datetime

'''
Make sure the required packages are installed: 
Open the Terminal in PyCharm (bottom left). 

On Windows type:
python -m pip install -r requirements.txt

On MacOS type:
pip3 install -r requirements.txt

This will install the packages from the requirements.txt for this project.
'''

app = Flask(__name__)
app.config['SECRET_KEY'] = '8BYkEfBA6O6donzWlSihBXox7C0sKR6b'
Bootstrap5(app)
ckeditor = CKEditor(app)

class EditForm(FlaskForm):
    title = StringField('The blog post title', validators=[DataRequired()])
    subtitle = StringField('The subtitle', validators=[DataRequired()])
    author = StringField("The author's name", validators=[DataRequired()])
    img_url = StringField('A URL for background image', validators=[DataRequired(), URL()])
    body = CKEditorField('Body', validators=[DataRequired()])
    submit = SubmitField('Submit Post')


# CREATE DATABASE
class Base(DeclarativeBase):
    pass
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///posts.db'
db = SQLAlchemy(model_class=Base)
db.init_app(app)


# CONFIGURE TABLE
class BlogPost(db.Model):
    id: Mapped[int] = mapped_column(Integer, primary_key=True)
    title: Mapped[str] = mapped_column(String(250), unique=True, nullable=False)
    subtitle: Mapped[str] = mapped_column(String(250), nullable=False)
    date: Mapped[str] = mapped_column(String(250), nullable=False)
    body: Mapped[str] = mapped_column(Text, nullable=False)
    author: Mapped[str] = mapped_column(String(250), nullable=False)
    img_url: Mapped[str] = mapped_column(String(250), nullable=False)


with app.app_context():
    db.create_all()


@app.route('/')
def get_all_posts():
    result = db.session.execute(db.select(BlogPost).order_by(BlogPost.id))
    posts = result.scalars()
    return render_template("index.html", all_posts=posts)

@app.route('/show_post/<int:post_id>')
def show_post(post_id):
    requested_post = db.session.execute(db.select(BlogPost).where(BlogPost.id == post_id)).scalar()
    print(requested_post.date)
    return render_template("post.html", post=requested_post)

@app.route('/new-post',methods=['GET', 'POST'])
def add_new_post():
    form = EditForm()
    current_date = datetime.now()
    formatted_date = current_date.strftime("%B %d, %Y")
    if request.method == "POST" and form.validate_on_submit():
        new_post = BlogPost(
            title = form.title.data,
            subtitle = form.subtitle.data,
            date = formatted_date,
            author = form.author.data,
            img_url = form.img_url.data,
            body = form.body.data
        )
        with app.app_context():
            db.session.add(new_post)
            db.session.commit()
        return get_all_posts()
    elif request.method == "GET":
        return render_template("make-post.html", form=form)

# TODO: edit_post() to change an existing blog post

@app.route('/edit-post/<int:post_id>',methods=['GET', 'POST'])
def edit_post(post_id):
    post_to_update = db.session.execute(db.select(BlogPost).where(BlogPost.id == post_id)).scalar()
    form = EditForm(
        title = post_to_update.title,
        subtitle = post_to_update.subtitle,
        author = post_to_update.author,
        img_url = post_to_update.img_url,
        body = post_to_update.body,
    )
    if request.method == "POST" and form.validate_on_submit():
        post_to_update.title = form.title.data
        post_to_update.subtitle = form.subtitle.data
        post_to_update.author = form.author.data
        post_to_update.img_url = form.img_url.data
        post_to_update.body = form.body.data
        with app.app_context():
            db.session.commit()
        return redirect(url_for("show_post", post_id=post.id))
    elif request.method == "GET":
        return render_template("make-post.html", form=form, post=post_to_update)

@app.route("/delete/<int:post_id>", methods=["GET"])
def delete_post(post_id):
    with app.app_context():
        post_to_delete = db.session.execute(db.select(BlogPost).where(BlogPost.id == post_id)).scalar()
        if request.method == "GET":
            db.session.delete(post_to_delete)
            db.session.commit()
            return redirect(url_for('get_all_posts'))

# Below is the code from previous lessons. No changes needed.
@app.route("/about")
def about():
    return render_template("about.html")


@app.route("/contact")
def contact():
    return render_template("contact.html")


if __name__ == "__main__":
    app.run(debug=True, port=5003)
