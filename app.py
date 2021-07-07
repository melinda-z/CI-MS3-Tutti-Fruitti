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


@app.route("/all_recipes")
def all_recipes():
    recipes = list(mongo.db.recipes.find())
    return render_template("all_recipes.html", recipes=recipes)


@app.route(("/full_recipe/<recipe_id>"))
def full_recipe(recipe_id):
    recipe = mongo.db.recipes.find_one({"_id": ObjectId(recipe_id)})
    try:
        category = mongo.db.categories.find_one({"_id": recipe["category_name"]})
        user = mongo.db.users.find_one({"_id": recipe["created_by"]})
        recipe["category_name"] = category["category_name"]
        recipe["created_by"] = user["username"]
    except Exception():
        pass
    return render_template("full_recipe.html", recipe=recipe)


@app.route("/my_recipes/<username>", methods=["GET", "POST"])
def my_recipes(username):
    # grab the session user's username from db
    username = mongo.db.users.find_one({"username": session["user"]})["username"]
    recipes = list(mongo.db.recipes.find())
    if session["user"]:
        return render_template("my_recipes.html", username=username, recipes=recipes)

    return redirect(url_for("log_in"))


@app.route("/log_in", methods=["GET", "POST"])
def log_in():
    if request.method == "POST":
        # Check if username already exists in db
        existing_user = mongo.db.users.find_one(
            {"username": request.form.get("username").lower()}
        )

        if existing_user:
            # ensure hashed password matches user input
            if check_password_hash(
                existing_user["password"], request.form.get("password")
            ):
                session["user"] = request.form.get("username").lower()
                flash(
                    "You are successfully logged in, {}!".format(
                        request.form.get("username").capitalize()
                    )
                )
                return redirect(url_for("my_recipes", username=session["user"]))

            else:
                # invalid password match
                flash("Incorrect Username and/or Password")
                return redirect(url_for("log_in"))

        else:
            #  username doesn't exist
            flash("Incorrect Username and/or Password")
            return redirect(url_for("log_in"))

    return render_template("log_in.html")


@app.route("/log_out")
def log_out():
    # remove user from session cookies
    flash("You have been logged out")
    session.pop("user")
    return redirect(url_for("log_in"))


@app.route("/register", methods=["GET", "POST"])
def register():
    if request.method == "POST":
        # Check if username already exists in db
        existing_user = mongo.db.users.find_one(
            {"username": request.form.get("username").lower()}
        )

        if existing_user:
            flash("Username already exists")
            return redirect(url_for("register"))

        register = {
            "username": request.form.get("username").lower(),
            "password": generate_password_hash(request.form.get("password")),
        }
        mongo.db.users.insert_one(register)

        # put the new user into "session" cookie
        session["user"] = request.form.get("username").lower()
        flash("Registration Successful!")
        return redirect(url_for("my_recipes", username=session["user"]))

    return render_template("register.html")


@app.route("/add_recipe", methods=["GET", "POST"])
def add_recipe():
    if request.method == "POST":
        user = mongo.db.users.find_one({"username": session["user"]})
        category = mongo.db.categories.find_one(
            {"category_name": request.form.get("category_name")}
        )
        recipe = {
            "category_name": ObjectId(category["_id"]),
            "smoothie_name": request.form.get("smoothie_name"),
            "ingredients": request.form.getlist("new-ingredient"),
            "method": request.form.get("method"),
            "image_url": request.form.get("image_url"),
            "created_by": ObjectId(user["_id"]),
        }
        mongo.db.recipes.insert_one(recipe)
        flash("Recipe Successfully Added")
        return redirect(url_for("my_recipes", username=session["user"]))
    categories = mongo.db.categories.find().sort("category_name", 1)
    return render_template("add_recipe.html", categories=categories)


@app.route("/edit_recipe/<recipe_id>", methods=["POST", "GET"])
def edit_recipe(recipe_id):
    if request.method == "POST":
        user = mongo.db.users.find_one({"username": session["user"]})
        category = mongo.db.categories.find_one(
            {"category_name": request.form.get("category_name")}
        )
        submit = {
            "category_name": ObjectId(category["_id"]),
            "smoothie_name": request.form.get("smoothie_name"),
            "ingredients": request.form.getlist("new-ingredient"),
            "method": request.form.get("method"),
            "image_url": request.form.get("image_url"),
            "created_by": ObjectId(user["_id"]),
        }
        mongo.db.recipes.update({"_id": ObjectId(recipe_id)}, submit)
        flash("Recipe Successfully Updated")
        return redirect(url_for("my_recipes", username=session["user"]))

    recipe = mongo.db.recipes.find_one({"_id": ObjectId(recipe_id)})
    categories = mongo.db.categories.find().sort("category_name", 1)
    return render_template("edit_recipe.html", recipe=recipe, categories=categories)


if __name__ == "__main__":
    app.run(host=os.environ.get("IP"), port=int(os.environ.get("PORT")), debug=True)
