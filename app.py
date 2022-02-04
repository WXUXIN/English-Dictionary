import os

from cs50 import SQL
from flask import Flask, flash, redirect, render_template, request, session
from flask_session import Session
from tempfile import mkdtemp
from werkzeug.security import check_password_hash, generate_password_hash

from helpers import  login_required

# Configure application
app = Flask(__name__)

# Ensure templates are auto-reloaded
app.config["TEMPLATES_AUTO_RELOAD"] = True

# Configure session to use filesystem (instead of signed cookies)
app.config["SESSION_PERMANENT"] = False
app.config["SESSION_TYPE"] = "filesystem"
Session(app)

# Configure CS50 Library to use SQLite database
db = SQL("sqlite:///project.db")

@app.after_request
def after_request(response):
    """Ensure responses aren't cached"""
    response.headers["Cache-Control"] = "no-cache, no-store, must-revalidate"
    response.headers["Expires"] = 0
    response.headers["Pragma"] = "no-cache"
    return response

@app.route("/")
@login_required
def index():
    rows = db.execute("SELECT words, notes, date, time FROM word WHERE id = ?", session["user_id"])
    return render_template("start.html", rows=rows)

@app.route("/search", methods=["GET", "POST"])
@login_required
def search():
    if request.method == "POST":
        # Keys in the values of words and notes into database
        if not request.form.get("word"):
            return render_template("searchfailure.html")

        date = db.execute("SELECT DATE() AS date")
        date1 = date[0]["date"]
        time = db.execute("SELECT TIME() AS time")
        time1 = time[0]["time"]
        db.execute("INSERT INTO word (id, words, notes, date, time) VALUES (?,?,?,?,?)",session["user_id"], request.form.get("word"), request.form.get("note"), date1, time1)
        return redirect("/")

    else:
        return render_template("search.html")

@app.route("/login", methods=["GET", "POST"])
def login():

    # Forget any user_id
    session.clear()
    #Log users into
    if request.method == "POST":

        # Ensure username was submitted
        if not request.form.get("username") or not request.form.get("password"):
            return render_template("failure.html")

        # Query database for username
        rows = db.execute("SELECT * FROM users WHERE username = ?", request.form.get("username"))

        # Ensure username exists and password is correct
        if len(rows) != 1 or not check_password_hash(rows[0]["hash"], request.form.get("password")):
            return render_template("failure.html")

        # Remember which user has logged in
        session["user_id"] = rows[0]["id"]

        # Redirect user to home page
        return redirect("/")

    # User reached route via GET (as by clicking a link or via redirect)
    else:
        return render_template("login.html")


@app.route("/register", methods=["GET", "POST"])
def register():
    """Register user"""
    if request.method == "POST":
        if not request.form.get("username"):
            return render_template("r1failure.html")

        elif db.execute("SELECT * FROM users WHERE username = ?", request.form.get("username")):
            return render_template("r2failure.html")

        if not request.form.get("password") or not request.form.get("confirmation") or (request.form.get("password") != request.form.get("confirmation")):
            return render_template("r3failure.html")

        if  len(request.form.get("password")) < 9:
            return render_template("r4failure.html")

        db.execute("INSERT INTO users (username, hash) VALUES(?, ?)",request.form.get("username"), generate_password_hash(request.form.get("password")))

        return redirect("/")

    else:
        return render_template("register.html")

@app.route("/logout")
def logout():
    """Log user out"""

    # Forget any user_id
    session.clear()

    # Redirect user to login form
    return redirect("/")