from flask import Flask, render_template, request
import requests
import os
import smtplib

# USE YOUR OWN npoint LINK! ADD AN IMAGE URL FOR YOUR POST. 👇
posts = requests.get("https://api.npoint.io/a6106642a85428ba0252").json()

app = Flask(__name__)

def send_mail(message, to_address):
   my_email = "maciek.kubat@gmail.com"
   password = os.environ.get("PASS")
   with smtplib.SMTP("smtp.gmail.com",port=587) as connection:
       connection.starttls()
       connection.login(user=my_email,password=password)
       connection.sendmail(
           from_addr=my_email,
           to_addrs=to_address,
           msg=f"Subject:Form Message\n\n{message}"
       )

@app.route('/')
def get_all_posts():
    return render_template("index.html", all_posts=posts)


@app.route("/about")
def about():
    return render_template("about.html")


@app.route("/contact", methods=["POST","GET"])
def contact():
    if request.method == "GET":
        return render_template("contact.html", title = "Message me")
    elif request.method == "POST":
        name = request.form["name"]
        email = request.form["email"]
        phone = request.form["phone"]
        message = request.form["message"]
        send_mail(f"{name}\n{email}\n{phone}\n{message}", "maciek.kubat@gmail.com")
        return render_template("contact.html", title = "Message sent")

@app.route("/post/<int:index>")
def show_post(index):
    requested_post = None
    for blog_post in posts:
        if blog_post["id"] == index:
            requested_post = blog_post
    return render_template("post.html", post=requested_post)


if __name__ == "__main__":
    app.run(debug=True, port=5001)
