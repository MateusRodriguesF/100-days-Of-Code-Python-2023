from flask import Flask, jsonify, render_template, request
from flask_sqlalchemy import SQLAlchemy
import random
#------------------------------App Init------------------------------------------
app = Flask(__name__)

# ---------------------------Connect to Database---------------------------------
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///cafes.db'
db = SQLAlchemy()
db.init_app(app)
#---------------------------Cafe TABLE Configuration------------------------------
class Cafe(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(250), unique=True, nullable=False)
    map_url = db.Column(db.String(500), nullable=False)
    img_url = db.Column(db.String(500), nullable=False)
    location = db.Column(db.String(250), nullable=False)
    seats = db.Column(db.String(250), nullable=False)
    has_toilet = db.Column(db.Boolean, nullable=False)
    has_wifi = db.Column(db.Boolean, nullable=False)
    has_sockets = db.Column(db.Boolean, nullable=False)
    can_take_calls = db.Column(db.Boolean, nullable=False)
    coffee_price = db.Column(db.String(250), nullable=True)
    #------------------------------result to dict function ------------------------------------------
    def to_dict(self): #transform a db return to dictionary
        return {column.name: getattr(self, column.name) for column in self.__table__.columns}
    # Optional: this will allow each book object to be identified by its title when printed.
    # def __repr__(self):
    #     return f'<Cafe {self.name}>'
with app.app_context():
    db.create_all()
#------------------------------Routes------------------------------------------
@app.route("/")
def home():
    return render_template("index.html")
#------------------------------Random Route------------------------------------------
# HTTP GET - Read Record
@app.route("/random", methods=["GET"])
def get_random_cafe():
    result = db.session.execute(db.select(Cafe))
    all_cafe = result.scalars().all()
    random_cafe = random.choice(all_cafe)    
    return jsonify(cafe=random_cafe.to_dict())
#------------------------------All Route------------------------------------------
# HTTP GET - Read Record
@app.route("/all", methods=["GET"]) #GET is allowed by default on all routes.
def all():
    result = db.session.execute(db.select(Cafe).order_by(Cafe.id))
    all_cafe = result.scalars().all()
    return jsonify(Cafes=[cafe.to_dict() for cafe in all_cafe])
#------------------------------Search Route------------------------------------------
@app.route("/search")
def search():
    query_location = request.args.get("loc") #Get the location value from the request
    result = db.session.execute(db.select(Cafe).where(Cafe.location == query_location))
    all_cafes = result.scalars().all()
    if all_cafes:
        return jsonify(cafes=[cafe.to_dict() for cafe in all_cafes]) # will return all the objects in the dictionary
    else:
        return jsonify(error={"Not Found": "Sorry, we don't have a cafe in that location."}),404
#------------------------------Add Route------------------------------------------
# HTTP POST - Create Record
@app.route("/add", methods=["POST"])
def post_new_cafe():
    new_cafe = Cafe(
    name = request.form.get("name"),
    map_url=request.form.get("map_url"),
    img_url=request.form.get("img_url"),
    location=request.form.get("loc"),
    has_sockets=bool(request.form.get("has_sockets")),
    has_toilet=bool(request.form.get("has_toilet")),
    has_wifi=bool(request.form.get("has_wifi")),
    can_take_calls=bool(request.form.get("can_take_calls")),
    seats=request.form.get("seats"),
    coffee_price=request.form.get("coffee_price"),
    )
    db.session.add(new_cafe)
    db.session.commit()
    return jsonify(response={"success":"Successfuly added the new cafe."})
#------------------------------Update Route------------------------------------------
# HTTP PUT/PATCH - Update Record
@app.route("/update-price/<int:cafe_id>", methods=["PATCH"])
def update_price(cafe_id):
    # cafe_id = request.arg.get("cafe_id")
    new_price = request.args.get("price")
    cafe_to_update = db.session.get(Cafe, cafe_id)
    if cafe_to_update:
        cafe_to_update.coffee_price = new_price
        db.session.commit()
        return jsonify(response={"success":"Successfuly aupdated the cafe price."}),200
    else:
        return jsonify(error={"Not":"Sorry, there isn't any cafe with this id"}),404
#------------------------------Delete Route------------------------------------------
# HTTP DELETE - Delete Record
@app.route("/report-closed/<int:cafe_id>", methods=["DELETE"])
def report_closed(cafe_id):
    TopSecretAPIKey = "*API_S3CR37@"
    api_key = request.args.get("api-key")
    if api_key == TopSecretAPIKey:
        cafe_to_delete = db.session.get(Cafe, cafe_id)
        if cafe_to_delete:
            db.session.delete(cafe_to_delete)
            db.session.commit()
            return jsonify(response={"success":"Successfuly deleted cafe from database."}),200
        else:
            return jsonify(error={"Not":"Sorry, there isn't any cafe with this id"}),404
    
    else:
        return jsonify(error={"Not":"Sorry, thats not allowed. Make sure You have the correct api_key"}),404

if __name__ == '__main__':
    app.run(debug=True)
