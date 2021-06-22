import os
from flask import Flask, flash, render_template, redirect, request, session, url_for
from flask_pymongo import PyMongo
from bson.objectid import ObjectId

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


@app.route("/register")
def register():
    return render_template("register.html")


@app.route("/login")
def login():
    return render_template("login.html")


@app.route("/recipes")
def recipes():
    return render_template("recipes.html")


@app.route("/profile")
def profile():
    return render_template("profile.html")


@app.route("/utensils")
def utensils():
    return render_template("utensils.html")


@app.route("/logout")
def logout():
    return render_template("logout.html")


@app.route("/detox")
def title():
    categories = mongo.db.categories.find()
    return render_template("detox.html", categories=categories)


if __name__ == "__main__":
    app.run(host=os.environ.get("IP"), port=int(os.environ.get("PORT")), debug=True)
