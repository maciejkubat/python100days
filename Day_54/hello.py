from flask import Flask

app = Flask(__name__)

def make_bold(function):
    def wrapper_function():
        return f"<b>{function()}</b>"
    return wrapper_function

def make_emphasis(function):
    def wrapper_function():
        return f"<em>{function()}</em>"
    return wrapper_function

def make_underline(function):
    def wrapper_function():
        return f"<u>{function()}</u>"
    return wrapper_function

@app.route("/")
def hello_world():
    return ('<h1 style="text-align: center">Hello, World!</h1>'
            '<p>Lorem ipsum</p>'
            '<img src="https://media3.giphy.com/media/v1.Y2lkPTc5MGI3NjExY2M4bnA2MjU2YmhsODFneWd6aHFkcjJ6MDRpb2YyOTR0c3FtZGN2eiZlcD12MV9pbnRlcm5hbF9naWZfYnlfaWQmY3Q9Zw/3oriO0OEd9QIDdllqo/giphy.gif" width=200>')

@app.route("/bye")
@make_bold
@make_emphasis
@make_underline
def bye():
    return "Bye"

@app.route("/<name>")
def greet(name):
    return f"Hello {name}"

if __name__ == "__main__":
    app.run(debug=True)