import os
from flask import Flask, flash, render_template, redirect, request, session, url_for
from flask_pymongo import PyMongo
from bson.objectid import ObjectId
from werkzeug.security import generate_password_hash, check_password_hash

if os.path.exists("env.py"):
    import env


app = Flask(__name__)


app.config["MONGO_DBNAME"] = os.environ.get("MONGO_DBNAME")
app.config["MONGO_URI"] = os.environ.get("MONGO_URI")
app.config["SECRET_KEY"] = os.environ.get("SECRET_KEY")

mongo = PyMongo(app)


@app.route("/")
def home():
    return render_template("home.html")


@app.route("/benefits")
def benefits():
    return render_template("benefits.html")


@app.route("/register", methods=["GET", "POST"])
def register():
    return render_template("register.html")


@app.route("/login")
def login():
    return render_template("login.html")


@app.route("/all_recipes")
def all_recipes():
    return render_template("all_recipes.html")


@app.route("/profile")
def profile():
    return render_template("profile.html")


@app.route("/utensils")
def utensils():
    return render_template("utensils.html")


@app.route("/logout")
def logout():
    return render_template("logout.html")


if __name__ == "__main__":
    app.run(host=os.environ.get("IP"), port=int(os.environ.get("PORT")), debug=True)
