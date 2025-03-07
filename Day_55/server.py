from flask import Flask
from random import randint

app = Flask(__name__)
drawn_number = randint(0,9)

@app.route("/")
def home():
    return ('<h1>Guess a number between 0 and 9</h1>'
            f'<p>Enter your guess after / in url</p>'
            '<img src="https://media.giphy.com/media/3o7aCSPqXE5C6T8tBC/giphy.gif">')

@app.route("/<int:number>")
def guess(number):
    if number > drawn_number:
        return ('<h1 style="color:red">Too high</h1>'
                '<img src="https://media.giphy.com/media/3o6ZtaO9BZHcOjmErm/giphy.gif">')
    if number < drawn_number:
        return ('<h1 style="color:blue">Too low</h1>'
                '<img src="https://media.giphy.com/media/jD4DwBtqPXRXa/giphy.gif">')
    else:
        return ('<h1 style="color:green">You found me</h1>'
                '<img src="https://media.giphy.com/media/4T7e4DmcrP9du/giphy.gif">')

if __name__ == "__main__":
    app.run(debug=True)