from random import choice
from flask import Flask, jsonify, render_template, request
from flask_sqlalchemy import SQLAlchemy
from sqlalchemy.orm import DeclarativeBase, Mapped, mapped_column
from sqlalchemy import Integer, String, Boolean
from sqlalchemy.sql import func


app = Flask(__name__)

API_KEY = "TopSecretApiKey"

# CREATE DB
class Base(DeclarativeBase):
    pass

app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///cafes.db'
db = SQLAlchemy(model_class=Base)
db.init_app(app)

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
        return {column.name: getattr(self, column.name) for column in self.__table__.columns}


with app.app_context():
    db.create_all()


@app.route("/")
def home():
    print(type(db))
    return render_template("index.html")

@app.route("/random")
def get_random_cafe():
    result = db.session.execute(db.select(Cafe))
    all_cafes = result.scalars().all()
    random_cafe = choice(all_cafes)
    return jsonify(cafe=random_cafe.to_dict())

@app.route("/all")
def get_all_cafes():
    result = db.session.execute(db.select(Cafe)).scalars().all()
    cafes = [cafe.to_dict() for cafe in result]
    return jsonify(cafes)

@app.route("/search/<location>")
def search(location):
    result = db.session.query(Cafe).filter(Cafe.location == location).all()
    filtered_cafes = [cafe.to_dict() for cafe in result]
    if len(filtered_cafes) > 0:
        return jsonify(filtered_cafes)
    else:
        return {
            "error": {
                "Not found": "Sorry, we did not found a cafe in that location."
            }
        }

@app.route("/add", methods=["POST"])
def add_new_cafe():
    data = request.get_json()

    if not data or not all(key in data for key in ["name", "map_url", "img_url", "loc", "coffee_price"]):
        return jsonify({"error": "Missing required fields in JSON"}), 400

    new_cafe = Cafe(
        name=data["name"],
        map_url=data["map_url"],
        img_url=data["img_url"],
        location=data["loc"],
        has_sockets=bool(data.get("sockets", False)),
        has_toilet=bool(data.get("toilet", False)),
        has_wifi=bool(data.get("wifi", False)),
        can_take_calls=bool(data.get("calls", False)),
        seats=data.get("seats", "Unknown"),
        coffee_price=data["coffee_price"],
    )

    db.session.add(new_cafe)
    db.session.commit()

    return jsonify(response={"success": "Successfully added the new cafe."}), 201

@app.route("/update-price/<cafe_id>/<new_price>", methods=["PATCH"])
def update(cafe_id, new_price):
    print(cafe_id)
    cafe = db.get_or_404(Cafe, cafe_id)
    if not cafe:
        return jsonify({"error": f"Cafe with id {cafe_id} not found"}), 404

    try:
        cafe.coffee_price = new_price
        db.session.commit()
        return jsonify({"success": f"Updated cafe id {cafe_id} with new price {new_price}"}), 200
    except Exception as e:
        db.session.rollback()
        return jsonify({"error": f"Failed to update price. Details: {str(e)}"}), 500


@app.route("/report-closed/<cafe_id>", methods=["DELETE"])
def delete(cafe_id):
    api_key = request.args.get("apiKey")
    if api_key != API_KEY:
        return jsonify({"error": "You are not allowed to delete from DB."}), 404

    cafe = db.get_or_404(Cafe, cafe_id)
    try:
        db.session.delete(cafe)
        db.session.commit()
        return jsonify({"success": f"Cafe with ID {cafe_id} has been deleted"}), 200
    except Exception as e:
        db.session.rollback()
        return jsonify({"error": f"An error occurred: {str(e)}"}), 500

if __name__ == '__main__':
    app.run(debug=True)
