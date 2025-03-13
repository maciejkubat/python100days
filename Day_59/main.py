from flask import Flask, render_template
import requests
from post import Post
from datetime import datetime

app = Flask(__name__)

current_year = datetime.now().year

blog_url = "https://api.npoint.io/a6106642a85428ba0252"
response = requests.get(blog_url)
response.raise_for_status()
all_posts = response.json()
all_posts_objects = []
for post in all_posts:
    object = Post(post_id=post["id"],title=post["title"],subtitle=post["subtitle"],body=post["body"],author=post["author"],date=post["date"], image_url=post["image_url"])
    all_posts_objects.append(object)

def get_object_by_post_id(objects, post_id):
    result = [obj for obj in objects if obj.id == post_id]
    return result[0] if result else None

@app.route('/')
def home():
    return render_template("index.html", posts=all_posts_objects, year=current_year)

@app.route('/post/<int:id>')
def get_post(id):
    return render_template("post.html", post=get_object_by_post_id(all_posts_objects,id), year=current_year)

@app.route('/about')
def about():
    return render_template("about.html", year=current_year)

@app.route('/contact')
def contact():
    return render_template("contact.html", year=current_year)

if __name__ == "__main__":
    app.run(debug=True)