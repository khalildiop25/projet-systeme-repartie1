from flask import Flask, jsonify
from flask_sqlalchemy import SQLAlchemy
from flask_cors import CORS
import os

app = Flask(__name__)

# Activer CORS
CORS(app)

# Configuration base de données
app.config['SQLALCHEMY_DATABASE_URI'] = os.getenv(
    "DATABASE_URL",
    "postgresql://postgres:postgres@db:5432/mydb"
)

app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

db = SQLAlchemy(app)

class User(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(100))


class Product(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(100))
    price = db.Column(db.Float)


@app.route("/")
def home():
    return "API Flask OK"


@app.route("/users")
def get_users():
    users = User.query.all()
    return jsonify([
        {"id": u.id, "name": u.name}
        for u in users
    ])


@app.route("/products")
def get_products():
    products = Product.query.all()
    return jsonify([
        {"id": p.id, "name": p.name, "price": p.price}
        for p in products
    ])


#run
if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000, debug=True)
