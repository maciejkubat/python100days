from flask import Flask, jsonify, render_template, request
from flask_sqlalchemy import SQLAlchemy
from sqlalchemy.orm import DeclarativeBase, Mapped, mapped_column
from sqlalchemy import Integer, String, Boolean, func

'''
Install the required packages first: 
Open the Terminal in PyCharm (bottom left). 

On Windows type:
python -m pip install -r requirements.txt

On MacOS type:
pip3 install -r requirements.txt

This will install the packages from requirements.txt for this project.
'''

app = Flask(__name__)

# CREATE DB
class Base(DeclarativeBase):
    pass
# Connect to Database
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///cafes.db'
db = SQLAlchemy(model_class=Base)
db.init_app(app)


# Cafe TABLE Configuration
class Cafe(db.Model):
    id: Mapped[int] = mapped_column(Integer, primary_key=True)
    name: Mapped[str] = mapped_column(String(250), unique=True, nullable=False)
    map_url: Mapped[str] = mapped_column(String(500), nullable=False)
    img_url: Mapped[str] = mapped_column(String(500), nullable=False)
    location: Mapped[str] = mapped_column(String(250), nullable=False)
    seats: Mapped[str] = mapped_column(String(250), nullable=False)
    has_toilet: Mapped[bool] = mapped_column(Boolean, nullable=False)
    has_wifi: Mapped[bool] = mapped_column(Boolean, nullable=False)
    has_sockets: Mapped[bool] = mapped_column(Boolean, nullable=False)
    can_take_calls: Mapped[bool] = mapped_column(Boolean, nullable=False)
    coffee_price: Mapped[str] = mapped_column(String(250), nullable=True)

    def to_dict(self):
        # Method 1.
        dictionary = {}
        # Loop through each column in the data record
        for column in self.__table__.columns:
            # Create a new dictionary entry;
            # where the key is the name of the column
            # and the value is the value of the column
            dictionary[column.name] = getattr(self, column.name)
        return dictionary

        # Method 2. Altenatively use Dictionary Comprehension to do the same thing.
        # return {column.name: getattr(self, column.name) for column in self.__table__.columns}

with app.app_context():
    db.create_all()


@app.route("/")
def home():
    return render_template("index.html")

# HTTP GET - Read Random Record

@app.route("/random", methods=["GET"])
def random():
    random_element = db.session.query(Cafe).order_by(func.random()).first()
    return jsonify(cafe = random_element.to_dict())

# HTTP GET - Read all records
@app.route("/all", methods=["GET"])
def cafes():
    result = db.session.execute(db.select(Cafe).order_by(Cafe.id))
    all_cafes = result.scalars()
    cafes_json = {"cafes" : []}
    for cafe in all_cafes:
        cafes_json["cafes"].append(cafe.to_dict())
    return jsonify(cafes_json)

# HTTP GET - Search

@app.route("/search", methods=["GET"])
def search():
    location = request.args.get('location')
    result = db.session.execute(db.select(Cafe).where(Cafe.location == location).order_by(Cafe.id))
    all_cafes = result.scalars()
    cafes_json = {"cafes" : []}
    for cafe in all_cafes:
        cafes_json["cafes"].append(cafe.to_dict())
    if cafes_json["cafes"]:
        return jsonify(cafes_json)
    else:
        return { "error" : { "Not Found" : "Sorry, we don't have a cafe at that location."}}, 404

# HTTP GET - Read Record

# HTTP POST - Create Record

@app.route("/add", methods=["POST"])
def add():
    data = request.get_json()
    new_cafe = Cafe(
        name = data.get('name'),
        map_url = data.get('map_url'),
        img_url = data.get('img_url'),
        location = data.get('location'),
        seats = data.get('seats'),
        has_toilet = data.get('has_toilet'),
        has_wifi = data.get('has_wifi'),
        has_sockets = data.get('has_sockets'),
        can_take_calls = data.get('can_take_calls'),
        coffee_price = data.get('coffee_price')
    )
    with app.app_context():
        db.session.add(new_cafe)
        db.session.commit()
    return jsonify(response = {"Success" : "It's the only option"})

# HTTP PUT/PATCH - Update Record

@app.route("/update_price/<int:index>", methods=["PATCH"])
def edit(index):
    data = request.get_json()
    price = data.get('coffee_price')
    cafe = db.session.query(Cafe).get(index)
    if cafe is None:
        return jsonify(error = {"Not Found" : "Sorry a cafe with that id was not found in the database."}), 404
    else:
        cafe.coffee_price = price
        db.session.commit()
        return {"success" : "Successfully updated the price."}, 200


# HTTP DELETE - Delete Record

@app.route("/report-closed/<int:index>", methods=["DELETE"])
def report_closed(index):
    api_key = request.args.get('api-key')
    cafe = db.session.query(Cafe).get(index)
    if cafe is None:
        return jsonify(error = {"Not Found" : "Sorry a cafe with that id was not found in the database."}), 404
    elif api_key == "MySecretApiKey":
        db.session.delete(cafe)
        db.session.commit()
        return {"success" : "Successfully Deleted."}, 200
    else:
        return {"forbidden": "You are unauthorised"}, 403

if __name__ == '__main__':
    app.run(debug=True)
