from flask import Flask, render_template
import random
from datetime import datetime
import requests

app = Flask(__name__)

@app.route("/")
def home():
    current_year = datetime.now().year
    random_number = random.randint(1, 10)
    return render_template("index.html", num = random_number, year = current_year)

@app.route("/guess/<name>")
def guess(name):
    name = name.capitalize()
    params = {
        "name" : name
    }
    response_gender = requests.get("https://api.genderize.io", params = params)
    response_gender.raise_for_status()
    data_gender = response_gender.json()
    gender = data_gender["gender"]
    response_age = requests.get("https://api.agify.io", params = params)
    response_age.raise_for_status()
    data_age = response_age.json()
    age = data_age["age"]
    return render_template("guess.html", name = name, gender = gender, age = age)

@app.route("/blog/<num>")
def get_blog(num):
    print(num)
    blog_url = "https://api.npoint.io/c790b4d5cab58020d391"
    response = requests.get(blog_url)
    response.raise_for_status()
    all_posts = response.json()
    return render_template("blog.html", posts=all_posts)


if __name__ == "__main__":
    app.run(debug=True)