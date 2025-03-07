from flask import Flask, render_template
from random import randint

app = Flask(__name__)
drawn_number = randint(0,9)

@app.route("/")
def home():
    return render_template("index.html")

if __name__ == "__main__":
    app.run(debug=True)