from flask import Flask, render_template
from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField
from wtforms.fields.simple import SubmitField
from wtforms.validators import DataRequired, Email, Length




'''
Red underlines? Install the required packages first: 
Open the Terminal in PyCharm (bottom left). 

On Windows type:
python -m pip install -r requirements.txt

On MacOS type:
pip3 install -r requirements.txt

This will install the packages from requirements.txt for this project.
'''


app = Flask(__name__)
app.secret_key = "any-string-you-want-just-keep-it-secret"

class MyForm(FlaskForm):
    email = StringField('Email', validators=[DataRequired(), Email()])
    password = PasswordField('Password', validators=[DataRequired(), Length(min=8)])
    submit = SubmitField(label="Log In")

@app.route("/")
def home():
    return render_template('index.html')

@app.route("/login",methods=["GET","POST"])
def login():
    form = MyForm()
    if form.validate_on_submit() and form.email.data == "admin@email.com" and form.password.data == "12345678":
        return render_template('success.html')
    else:
        return render_template('denied.html')

if __name__ == '__main__':
    app.run(debug=True)
