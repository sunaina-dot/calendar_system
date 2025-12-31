from flask import Blueprint, render_template, request, redirect
from flask_login import login_user
from models.user import User

auth_bp = Blueprint("auth", __name__)

@auth_bp.route("/", methods=["GET", "POST"])
def login():
    if request.method == "POST":
        user = User(id=1)   
        login_user(user)
        return redirect("/calendar")
    return render_template("auth/login.html")

@auth_bp.route("/register", methods=["GET", "POST"])
def register():
    if request.method == "POST":
        
        return redirect("/")
    return render_template("auth/register.html")
from flask import Blueprint, render_template, request, redirect, flash
from flask_login import login_user, logout_user
from models.user import User, get_user_by_username, create_user

auth_bp = Blueprint("auth", __name__)


@auth_bp.route("/", methods=["GET", "POST"])
def login():
    if request.method == "POST":
        username = request.form["username"]
        password = request.form["password"]

        user = get_user_by_username(username)

        if user and user["password"] == password:
            login_user(User(user["id"], user["username"]))
            return redirect("/calendar")

        flash("Invalid username or password")

    return render_template("auth/login.html")



@auth_bp.route("/register", methods=["GET", "POST"])
def register():
    if request.method == "POST":
        fullname = request.form["fullname"]
        username = request.form["username"]
        email = request.form["email"]
        password = request.form["password"]

        if get_user_by_username(username):
            flash("User already exists")
            return redirect("/register")

        create_user(fullname, username, email, password)
        flash("Registration successful. Please login.")
        return redirect("/")

    return render_template("auth/register.html")



@auth_bp.route("/logout")
def logout():
    logout_user()
    return redirect("/")
