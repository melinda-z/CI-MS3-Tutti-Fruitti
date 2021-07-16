import os
from flask import Flask, flash, render_template, redirect, request, session, url_for
from flask_pymongo import PyMongo
from bson.objectid import ObjectId
from werkzeug.security import generate_password_hash, check_password_hash
from flask_paginate import Pagination, get_page_args

if os.path.exists("env.py"):
    import env


app = Flask(__name__)


app.config["MONGO_DBNAME"] = os.environ.get("MONGO_DBNAME")
app.config["MONGO_URI"] = os.environ.get("MONGO_URI")
app.config["SECRET_KEY"] = os.environ.get("SECRET_KEY")

mongo = PyMongo(app)

# HOME PAGE
@app.route("/")
def home():
    """
    Display the home landing page
    """
    return render_template("home.html")


# ALL RECIPES PAGE
# Pagination
# https://gist.github.com/mozillazg/69fb40067ae6d80386e10e105e6803c9
# https://stackoverflow.com/questions/27992413/how-do-i-calculate-the-offsets-for-pagination/27992616

PER_PAGE = 6


def paginate(recipes):
    """
    Display relavent recipes on each page
    """
    page, _, offset = get_page_args(
        page_parameter="page", per_page_parameter="per_page"
    )
    offset = page * PER_PAGE - PER_PAGE

    return recipes[offset : offset + PER_PAGE]


def pagination_args(recipes):
    """
    Get and display the total number of pages
    """
    page, _, _ = get_page_args(page_parameter="page", per_page_parameter="per_page")
    total = len(recipes)

    return Pagination(page=page, per_page=PER_PAGE, total=total)


# All recipes page for all users
@app.route("/all_recipes")
def all_recipes():
    """
    Display recipes from the database, seperate with pages
    """
    recipes = list(mongo.db.recipes.find())
    paginated_recipes = paginate(recipes)
    pagination = pagination_args(recipes)

    return render_template(
        "all_recipes.html",
        recipes=paginated_recipes,
        pagination=pagination,
    )


# Search function in all recipes page for all users
@app.route("/search", methods=["GET", "POST"])
def search():
    """
    Allow users to search recipes using keyword
    """
    query = request.form.get("query")
    recipes = list(mongo.db.recipes.find({"$text": {"$search": query}}))

    paginated_recipes = paginate(recipes)
    pagination = pagination_args(recipes)

    return render_template(
        "all_recipes.html",
        recipes=paginated_recipes,
        pagination=pagination,
        query=query,
    )


# FULL RECIPE PAGE
# Full recipe displage page for all users
@app.route(("/full_recipe/<recipe_id>"))
def full_recipe(recipe_id):
    """
    Display full recipes details to the user
    """
    try:
        # assign _id with relative key name
        recipe = mongo.db.recipes.find_one({"_id": ObjectId(recipe_id)})
        category = mongo.db.categories.find_one({"_id": recipe["category_name"]})
        user = mongo.db.users.find_one({"_id": recipe["created_by"]})
        # reassign key name to readable category & user name
        recipe["category_name"] = category["category_name"]
        recipe["created_by"] = user["username"]
    except Exception():
        pass
    return render_template("full_recipe.html", recipe=recipe)


# USER ACCOUNT

# Register page
@app.route("/register", methods=["GET", "POST"])
def register():
    """
    Register and create an account for the user
    """
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


# Log in page for registered users
@app.route("/log_in", methods=["GET", "POST"])
def log_in():
    """
    user authenticathion check and log user into their account
    """
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


# My recipes page only for registered users
@app.route("/my_recipes/<username>", methods=["GET", "POST"])
def my_recipes(username):
    """
    Display user profile page and recipes created by them
    Upload recipe access
    """
    # grab the session user's username from db
    username = mongo.db.users.find_one({"username": session["user"]})["username"]
    # only display recipes created by current user
    user = mongo.db.users.find_one({"username": session["user"]})
    recipes = list(mongo.db.recipes.find({"created_by": ObjectId(user["_id"])}))

    # Pagination
    paginated_recipes = paginate(recipes)
    pagination = pagination_args(recipes)

    if session["user"]:
        return render_template(
            "my_recipes.html",
            username=username,
            recipes=paginated_recipes,
            pagination=pagination,
        )

    return redirect(url_for("log_in"))


# Log out function
@app.route("/log_out")
def log_out():
    """
    Allow user to log out
    """
    # remove user from session cookies
    flash("You have been logged out")
    session.pop("user")
    return redirect(url_for("log_in"))


# Allow logged in user to upload recipe page
@app.route("/add_recipe", methods=["GET", "POST"])
def add_recipe():
    """
    Allow user to add recipe by fill up the form
    and send it to database
    """
    if request.method == "POST":
        user = mongo.db.users.find_one({"username": session["user"]})
        category = mongo.db.categories.find_one(
            {"category_name": request.form.get("category_name")}
        )
        # create recipe using ObjectId for category name and created by
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


# Allow recipe loader to edit recipe page
@app.route("/edit_recipe/<recipe_id>", methods=["GET", "POST"])
def edit_recipe(recipe_id):
    """
    Allow user to edit the recipe they created
    and update it in the database
    """
    if request.method == "POST":
        user = mongo.db.users.find_one({"username": session["user"]})
        category = mongo.db.categories.find_one(
            {"category_name": request.form.get("category_name")}
        )

        update_recipe = {
            "category_name": ObjectId(category["_id"]),
            "smoothie_name": request.form.get("smoothie_name"),
            "ingredients": request.form.getlist("new-ingredient"),
            "method": request.form.get("method"),
            "image_url": request.form.get("image_url"),
            "created_by": ObjectId(user["_id"]),
        }

        mongo.db.recipes.update({"_id": ObjectId(recipe_id)}, update_recipe)
        flash("Recipe Successfully Updated")
        return redirect(url_for("my_recipes", username=session["user"]))

    recipe = mongo.db.recipes.find_one({"_id": ObjectId(recipe_id)})
    categories = mongo.db.categories.find().sort("category_name", 1)
    return render_template("edit_recipe.html", recipe=recipe, categories=categories)


# Allow recipe loader to delete recipe function
@app.route("/delete_recipe/<recipe_id>")
def delete_recipe(recipe_id):
    """
    Allow user to delete the recipes they have created
    and remove them from the database
    """
    mongo.db.recipes.remove({"_id": ObjectId(recipe_id)})
    flash("Recipe Successfully Deleted")
    return redirect(url_for("my_recipes", username=session["user"]))


# Admin Categories Management pages:

# Main page to display all categories to admin
@app.route("/get_categories")
def get_categories():
    """
    Get all the categories stored from the database
    with edit and delete button options
    """
    categories = list(mongo.db.categories.find().sort("category_name", 1))
    return render_template("categories.html", categories=categories)


# Allow admin to add category
@app.route("/add_category", methods=["GET", "POST"])
def add_category():
    """
    Allow admin to add category to the database
    """
    if request.method == "POST":
        category = {"category_name": request.form.get("category_name")}
        mongo.db.categories.insert_one(category)
        flash("New Category Added")
        return redirect(url_for("get_categories"))

    return render_template("add_category.html")


# Allow admin to edit category
@app.route("/edit_category/<category_id>", methods=["GET", "POST"])
def edit_category(category_id):
    """
    Allow admin to edit the category exists in the database
    """
    if request.method == "POST":
        submit = {"category_name": request.form.get("category_name")}
        mongo.db.categories.update({"_id": ObjectId(category_id)}, submit)
        flash("Category Successfully Updated")
        return redirect(url_for("get_categories"))

    category = mongo.db.categories.find_one({"_id": ObjectId(category_id)})
    return render_template("edit_category.html", category=category)


# Allow admin to delete category
@app.route("/delete_category/<category_id>")
def delete_category(category_id):
    """
    Allow admin to delete the categories saved in the datebase
    """
    mongo.db.categories.remove({"_id": ObjectId(category_id)})
    flash("Category Sucessfully Deleted")
    return redirect(url_for("get_categories"))


# Error handling
# https://flask.palletsprojects.com/en/2.0.x/errorhandling/
@app.errorhandler(403)
def forbidden(e):
    """
    403 error handler
    """
    return render_template("403.html"), 403


@app.errorhandler(404)
def page_not_found(e):
    """
    404 error handler
    """
    return render_template("404.html"), 404


@app.errorhandler(500)
def internal_server_error(e):
    """
    500 error handler
    """
    return render_template("errors/500.html"), 500


if __name__ == "__main__":
    app.run(host=os.environ.get("IP"), port=int(os.environ.get("PORT")), debug=True)
